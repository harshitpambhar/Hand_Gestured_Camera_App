import cv2
import math

def draw_capture_button(frame, cursor_x, cursor_y, click_event):
    # button geometry
    h, w, _ = frame.shape
    cx, cy = w // 2, h - 80
    radius = 30

    # draw button
    cv2.circle(frame, (cx, cy), radius, (255, 255, 255), 2)
    cv2.circle(frame, (cx, cy), radius - 4, (0, 0, 255), -1)

    # hit test
    dist = math.sqrt((cursor_x - cx)**2 + (cursor_y - cy)**2)
    hovered = dist <= radius

    if hovered and click_event:
        return True  # button pressed

    return False
