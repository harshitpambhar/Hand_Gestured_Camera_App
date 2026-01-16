import cv2
import numpy as np


def apply_none(frame):
    return frame


def apply_grayscale(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def apply_blur(frame, ksize=15):
    blur = cv2.GaussianBlur(frame, (ksize, ksize), 0)
    return blur


def apply_sepia(frame):
    kernel = np.array(
        [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]
    )
    sepia = cv2.transform(frame, kernel)
    return np.clip(sepia, 0, 255).astype("uint8")


def apply_edges(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
