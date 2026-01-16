import cv2
import os
import math
import numpy as np

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(project_root, "assets", "icons", "filtersoption.png")

filter_icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)

if filter_icon is None:
    raise FileNotFoundError(f"Icon not found at: {icon_path}")

ICON_H, ICON_W = filter_icon.shape[:2]  # 60, 300


def draw_filter_menu(frame, cursor_x, cursor_y, click_event, current_filter="NONE"):
    h, w, _ = frame.shape

    # Position: left of capture button
    x = w // 2 - ICON_W - 140
    y = h - ICON_H - 50

    # ---- Bounds check ----
    if x < 0 or y < 0 or x + ICON_W > w or y + ICON_H > h:
        return None

    # ---- Alpha blending ----
    icon_rgb = filter_icon[:, :, :3]

    # Check if alpha channel exists
    if filter_icon.shape[2] == 4:
        alpha = filter_icon[:, :, 3] / 255.0
    else:
        # No alpha channel, use full opacity
        alpha = np.ones((ICON_H, ICON_W))

    roi = frame[y : y + ICON_H, x : x + ICON_W]

    for c in range(3):
        roi[:, :, c] = alpha * icon_rgb[:, :, c] + (1 - alpha) * roi[:, :, c]

    # ---- Divide into sections ----
    filters = ["CANNY", "SEPIA", "BLUR", "GRAYSCALE"]
    section_width = ICON_W // 4

    # ---- Rectangular hit test ----
    hovered = x <= cursor_x <= x + ICON_W and y <= cursor_y <= y + ICON_H
    hovered_index = -1

    if hovered:
        relative_x = cursor_x - x
        hovered_index = relative_x // section_width

    # ---- Draw highlights for each section ----
    for i, filter_name in enumerate(filters):
        section_x = x + i * section_width

        # Highlight the currently selected filter (green border)
        if filter_name == current_filter:
            cv2.rectangle(
                frame,
                (section_x, y),
                (section_x + section_width, y + ICON_H),
                (0, 255, 0),  # Green for selected
                3,
            )

        # Highlight hovered section (yellow border)
        elif i == hovered_index:
            cv2.rectangle(
                frame,
                (section_x, y),
                (section_x + section_width, y + ICON_H),
                (0, 255, 255),  # Yellow for hover
                2,
            )

    # ---- Handle click ----
    if hovered and click_event:
        if 0 <= hovered_index < len(filters):
            return filters[hovered_index]

    return None
