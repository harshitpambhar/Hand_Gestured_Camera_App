import cv2
import time

from camera.camera_feed import open_camera
from gestures.hand_tracker import process_frame
from gestures.pinch import detect_pinch
from utils.math_utils import calculate_distance
from ui.capture_button import draw_capture_button
from ui.flip_camera import draw_flip_button
from ui.video_button import draw_video_button
from ui.filters_icon import draw_filter_button
from ui.filters_menu import draw_filter_menu
from ui.close_button import draw_close_button
from actions.capture import capture_frame
from actions.record import toggle_recording, get_recording_status
from filters.basic_filters import (
    apply_sepia,
    apply_grayscale,
    apply_blur,
    apply_none,
    apply_edges,
)


# ---------------- CAMERA SETUP ----------------
cap = open_camera()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Live Preview (PRESS 'q' to Quit)", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Preview (PRESS 'q' to Quit)", 1280, 720)

# ---------------- STATE VARIABLES ----------------
prev_pinched = False

# capture delay state
capture_pending = False
capture_start_time = None
capture_delay = 3  # seconds

# flip state
flip_enabled = False

# filters button
filter_menu_open = False
current_filter = "NONE"
filters_button_locked = False
filters_button_was_hovered = False
filter_option_locked = False

# video recording
video_button_locked = False

# close button
close_button_locked = False


# ================= MAIN LOOP =================
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame not received")
        break

    # ---- clean frame (NEVER draw UI here) ----
    clean_frame = frame.copy()

    # ---- apply flip ONLY to display frame ----
    if flip_enabled:
        frame = cv2.flip(frame, 1)
        clean_frame = cv2.flip(clean_frame, 1)

    # ---- hand tracking on original frame (BEFORE filters) ----
    result = process_frame(frame)

    cursor_x, cursor_y = -1, -1
    click_event = False

    # ---------------- HAND TRACKING ----------------
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            h, w, _ = frame.shape

            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

            cursor_x, cursor_y = ix, iy

            distance = calculate_distance(
                index_tip.x, index_tip.y, thumb_tip.x, thumb_tip.y
            )

            # cursor visuals (optional)
            cv2.circle(frame, (ix, iy), 15, (0, 0, 255), -1)
            cv2.circle(frame, (tx, ty), 15, (0, 0, 255), -1)

            prev_pinched, click_event = detect_pinch(distance, prev_pinched)

    # ---- apply selected filter AFTER hand tracking ----
    # Apply to both display frame and clean frame (for capture/recording)
    if current_filter == "SEPIA":
        frame = apply_sepia(frame)
        clean_frame = apply_sepia(clean_frame)
    elif current_filter == "GRAYSCALE":
        frame = apply_grayscale(frame)
        clean_frame = apply_grayscale(clean_frame)
    elif current_filter == "BLUR":
        frame = apply_blur(frame)
        clean_frame = apply_blur(clean_frame)
    elif current_filter == "CANNY":
        frame = apply_edges(frame)
        clean_frame = apply_edges(clean_frame)
    else:
        frame = apply_none(frame)
        clean_frame = apply_none(clean_frame)

    # ---------------- UI BUTTONS ----------------
    capture_pressed = draw_capture_button(frame, cursor_x, cursor_y, click_event)
    flip_pressed = draw_flip_button(frame, cursor_x, cursor_y, click_event)
    filters_button_pressed = draw_filter_button(frame, cursor_x, cursor_y, click_event)
    video_button_pressed = draw_video_button(frame, cursor_x, cursor_y, click_event)
    close_button_pressed = draw_close_button(frame, cursor_x, cursor_y, click_event)

    # ---- flip toggle ----
    if flip_pressed:
        flip_enabled = not flip_enabled

    # ---- close button ----
    if close_button_pressed and click_event and not close_button_locked:
        print("🚪 Closing application...")
        # Stop recording if active
        if get_recording_status():
            from actions.record import recorder

            recorder.stop_recording()
        # Break the main loop to close
        break

    # Unlock when finger leaves button area
    if not close_button_pressed:
        close_button_locked = False

    # ---- video recording toggle ----
    if video_button_pressed and click_event and not video_button_locked:
        toggle_recording(clean_frame)
        video_button_locked = True

    # Unlock when finger leaves button area
    if not video_button_pressed:
        video_button_locked = False

    # ---- write frame to video if recording ----
    if get_recording_status():
        from actions.record import recorder

        recorder.write_frame(clean_frame)

    # ---------------- FILTER BUTTON TOGGLE ----------------
    # Detect hover over filter button (reuse your draw function logic)
    filter_button_hovered = filters_button_pressed  # pressed implies hovered

    # Toggle ONLY on press edge
    if filter_button_hovered and click_event and not filters_button_locked:
        if filter_menu_open:
            # If menu is open, close it and reset to NONE
            filter_menu_open = False
            current_filter = "NONE"
        else:
            # If menu is closed, open it
            filter_menu_open = True
        filters_button_locked = True

    # Unlock ONLY when finger leaves button area
    if not filter_button_hovered:
        filters_button_locked = False

    # ---------------- FILTER MENU ----------------
    selected_filter = None

    if filter_menu_open:
        # Only allow selection on a NEW click
        if click_event and not filter_option_locked:
            selected_filter = draw_filter_menu(
                frame, cursor_x, cursor_y, click_event, current_filter
            )
            filter_option_locked = True
        else:
            selected_filter = draw_filter_menu(
                frame, cursor_x, cursor_y, False, current_filter
            )

    # Unlock when finger released
    if not click_event:
        filter_option_locked = False

    if selected_filter is not None:
        current_filter = selected_filter
        filter_menu_open = False

    # ---- start capture countdown ----
    if capture_pressed and not capture_pending:
        capture_pending = True
        capture_start_time = time.time()

    # ---- recording indicator ----
    if get_recording_status():
        cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        cv2.putText(
            frame,
            "REC",
            (50, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )

    # ---- countdown + capture ----
    if capture_pending:
        elapsed_time = time.time() - capture_start_time
        remaining_time = int(capture_delay - elapsed_time)

        if remaining_time > 0:
            cv2.putText(
                frame,
                str(remaining_time),
                (frame.shape[1] // 2 - 20, frame.shape[0] // 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 255),
                5,
            )

        if elapsed_time >= capture_delay:
            success, saved_path = capture_frame(clean_frame)
            if success:
                print(f"📸 Image saved at {saved_path}")

            capture_pending = False
            capture_start_time = None

    # ---------------- DISPLAY ----------------
    cv2.imshow("Live Preview (PRESS 'q' to Quit)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Quitting....")
        break

cv2.destroyAllWindows()
