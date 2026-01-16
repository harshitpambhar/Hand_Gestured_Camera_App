import cv2
import os
import math
import numpy as np

# Get the icon path relative to project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(project_root, "assets", "icons", "video_icon.png")

video_icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
ICON_SIZE = 60


def draw_video_button(frame, cursor_x, cursor_y, click_event):

    h, w, _ = frame.shape

    # Position: left of capture button
    x = w // 2 + 180
    y = h - ICON_SIZE - 50

    # --- Draw icon with transparency ---
    icon_rgb = video_icon[:, :, :3]

    # Check if alpha channel exists
    if video_icon.shape[2] == 4:
        alpha = video_icon[:, :, 3] / 255.0
    else:
        # No alpha channel, use full opacity
        alpha = np.ones((ICON_SIZE, ICON_SIZE))

    roi = frame[y : y + ICON_SIZE, x : x + ICON_SIZE]

    for c in range(3):
        roi[:, :, c] = alpha * icon_rgb[:, :, c] + (1 - alpha) * roi[:, :, c]

    # --- Hit test (circular for better UX) ---
    cx = x + ICON_SIZE // 2
    cy = y + ICON_SIZE // 2
    radius = ICON_SIZE // 2

    dist = math.sqrt((cursor_x - cx) ** 2 + (cursor_y - cy) ** 2)
    hovered = dist <= radius

    if hovered and click_event:
        return True

    return False
