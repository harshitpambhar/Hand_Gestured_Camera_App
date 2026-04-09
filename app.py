import cv2
import time
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

from gestures.hand_tracker import process_frame
from gestures.pinch import detect_pinch
from utils.math_utils import calculate_distance
from filters.basic_filters import apply_sepia, apply_grayscale, apply_blur, apply_edges, apply_none
from actions.capture import capture_frame

st.set_page_config(page_title="Hand Gesture Camera App", layout="wide")
st.title("📸 Hand Gesture Camera App")

# ---------------- SIDEBAR CONTROLS ----------------
st.sidebar.title("Controls")

selected_filter = st.sidebar.selectbox(
    "🎨 Filter", ["NONE", "SEPIA", "GRAYSCALE", "BLUR", "CANNY"]
)

flip_enabled = st.sidebar.checkbox("🔄 Flip Camera")

capture_btn = st.sidebar.button("📷 Capture Photo")

if "recording" not in st.session_state:
    st.session_state.recording = False

record_label = "⏹ Stop Recording" if st.session_state.recording else "🎥 Start Recording"
if st.sidebar.button(record_label):
    st.session_state.recording = not st.session_state.recording

st.sidebar.markdown("---")
st.sidebar.markdown("**Gesture:** Pinch thumb + index finger to interact")

# ---------------- VIDEO PROCESSOR ----------------
class CameraProcessor(VideoProcessorBase):
    def __init__(self):
        self.filter = "NONE"
        self.flip = False
        self.prev_pinched = False
        self.capture_now = False
        self.captured_frame = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        if self.flip:
            img = cv2.flip(img, 1)

        clean = img.copy()

        # Hand tracking
        result = process_frame(img)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]
                h, w, _ = img.shape
                ix, iy = int(index_tip.x * w), int(index_tip.y * h)
                tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

                distance = calculate_distance(index_tip.x, index_tip.y, thumb_tip.x, thumb_tip.y)
                self.prev_pinched, click = detect_pinch(distance, self.prev_pinched)

                cv2.circle(img, (ix, iy), 15, (0, 0, 255), -1)
                cv2.circle(img, (tx, ty), 15, (0, 0, 255), -1)

        # Apply filter
        filter_map = {
            "SEPIA": apply_sepia,
            "GRAYSCALE": apply_grayscale,
            "BLUR": apply_blur,
            "CANNY": apply_edges,
        }
        if self.filter in filter_map:
            img = filter_map[self.filter](img)
            clean = filter_map[self.filter](clean)

        # Capture
        if self.capture_now:
            self.captured_frame = clean.copy()
            self.capture_now = False

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# ---------------- WEBRTC STREAMER ----------------
ctx = webrtc_streamer(
    key="camera",
    video_processor_factory=CameraProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

# ---------------- SYNC CONTROLS TO PROCESSOR ----------------
if ctx.video_processor:
    ctx.video_processor.filter = selected_filter
    ctx.video_processor.flip = flip_enabled

    if capture_btn:
        ctx.video_processor.capture_now = True
        time.sleep(0.2)
        if ctx.video_processor.captured_frame is not None:
            success, path = capture_frame(ctx.video_processor.captured_frame)
            if success:
                st.sidebar.success(f"📸 Saved: {path}")
