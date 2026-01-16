import cv2
import os
import time

# Get project root (cameraApp/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class VideoRecorder:
    def __init__(self, frame_width=1280, frame_height=720, fps=30, save_dir="captures"):
        """
        Initialize video recorder with specified parameters.

        Args:
            frame_width: Video frame width
            frame_height: Video frame height
            fps: Frames per second
            save_dir: Directory to save videos
        """
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.fps = fps
        self.save_dir = os.path.join(PROJECT_ROOT, save_dir)

        # Create directory if it doesn't exist
        os.makedirs(self.save_dir, exist_ok=True)

        self.is_recording = False
        self.video_writer = None
        self.video_path = None

    def start_recording(self):
        """Start a new video recording session."""
        if self.is_recording:
            print("⚠️ Already recording")
            return False

        # Create filename with timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"video_{timestamp}.mp4"
        self.video_path = os.path.join(self.save_dir, filename)

        # Define codec and create VideoWriter
        # Using mp4v codec for better compatibility
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.video_writer = cv2.VideoWriter(
            self.video_path, fourcc, self.fps, (self.frame_width, self.frame_height)
        )

        if not self.video_writer.isOpened():
            print(f"❌ Failed to open video writer at {self.video_path}")
            self.video_writer = None
            return False

        self.is_recording = True
        print(f"🎥 Recording started: {self.video_path}")
        return True

    def write_frame(self, frame):
        """
        Write a frame to the video file.

        Args:
            frame: The frame to write (should be frame_width x frame_height)

        Returns:
            True if successful, False otherwise
        """
        if not self.is_recording or self.video_writer is None:
            return False

        self.video_writer.write(frame)
        return True

    def stop_recording(self):
        """Stop recording and save the video file."""
        if not self.is_recording:
            print("⚠️ Not currently recording")
            return False

        if self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None

        self.is_recording = False
        print(f"✅ Video saved: {self.video_path}")
        return True


# Global recorder instance
recorder = VideoRecorder()


def toggle_recording(frame):
    """
    Toggle recording on/off.

    Args:
        frame: Current camera frame to write if recording

    Returns:
        True if now recording, False if now stopped, None if error
    """
    if not recorder.is_recording:
        # Start recording
        return recorder.start_recording()
    else:
        # Write frame if recording
        recorder.write_frame(frame)
        # Stop recording
        return not recorder.stop_recording()


def get_recording_status():
    """Get current recording status."""
    return recorder.is_recording
