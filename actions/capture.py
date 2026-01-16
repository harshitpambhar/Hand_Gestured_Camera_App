import cv2
import os
import time

# Get project root (cameraApp/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def capture_frame(clean_frame, save_dir="captures"):
    """
    Saves a clean camera frame to disk.
    This function MUST NOT contain delay logic.
    """

    # Absolute save directory
    save_path = os.path.join(PROJECT_ROOT, save_dir)

    # Create directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    # Unique filename using timestamp
    # Use a filename-safe timestamp (avoid %D which adds slashes on Windows)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"capture_{timestamp}.jpg"
    filepath = os.path.join(save_path, filename)

    # Save image
    success = cv2.imwrite(filepath, clean_frame)

    return success, filepath
