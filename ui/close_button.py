import cv2
import os
import math
import numpy as np

# Get the icon path relative to project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(project_root, "assets", "icons", "cross.png")

close_icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
ICON_SIZE = 40  # Smaller size for close button

# Resize icon to match ICON_SIZE
if close_icon is not None:
    close_icon = cv2.resize(
        close_icon, (ICON_SIZE, ICON_SIZE), interpolation=cv2.INTER_AREA
    )


def draw_close_button(frame, cursor_x, cursor_y, click_event):
    """Draw close button in top-right corner."""
    h, w, _ = frame.shape

    # Position: top-right corner with padding
    x = w - ICON_SIZE - 20
    y = 20

    # --- Draw icon with transparency ---
    if close_icon is None:
        # Fallback: draw a red X if icon not found
        cv2.line(frame, (x, y), (x + ICON_SIZE, y + ICON_SIZE), (0, 0, 255), 3)
        cv2.line(frame, (x + ICON_SIZE, y), (x, y + ICON_SIZE), (0, 0, 255), 3)
    else:
        icon_rgb = close_icon[:, :, :3]

        # Check if alpha channel exists
        if close_icon.shape[2] == 4:
            alpha = close_icon[:, :, 3] / 255.0
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

    # Draw hover effect
    if hovered:
        cv2.circle(frame, (cx, cy), radius + 2, (0, 0, 255), 2)

    if hovered and click_event:
        return True

    return False
