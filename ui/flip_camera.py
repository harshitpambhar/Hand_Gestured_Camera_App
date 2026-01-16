import cv2
import os
import math

# Get the icon path relative to project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(project_root, "assets", "icons", "flip-camera-icon.png")

# Load icon with alpha channel
camera_icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)

ICON_SIZE = 60
camera_icon = cv2.resize(camera_icon, (ICON_SIZE, ICON_SIZE))


def draw_flip_button(frame, cursor_x, cursor_y, click_event):
    """
    Draws flip icon button and checks for click.
    Returns True if button is pressed.
    """

    h, w, _ = frame.shape

    # Position: right of capture button
    x = w // 2 + 80
    y = h - ICON_SIZE - 50

    # --- Draw icon with transparency ---
    icon_rgb = camera_icon[:, :, :3]
    alpha = camera_icon[:, :, 3] / 255.0

    roi = frame[y:y+ICON_SIZE, x:x+ICON_SIZE]

    for c in range(3):
        roi[:, :, c] = (
            alpha * icon_rgb[:, :, c] +
            (1 - alpha) * roi[:, :, c]
        )

    # --- Hit test (circular for better UX) ---
    cx = x + ICON_SIZE // 2
    cy = y + ICON_SIZE // 2
    radius = ICON_SIZE // 2

    dist = math.sqrt((cursor_x - cx) ** 2 + (cursor_y - cy) ** 2)
    hovered = dist <= radius

    if hovered and click_event:
        return True

    return False
