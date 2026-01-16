import mediapipe as mp
import cv2

# MediaPipe Hands setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,  # video stream
    max_num_hands=1,  # detect only 1 hand (stable)
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)

def process_frame(frame):
    # Convert BGR (OpenCV) to RGB (MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe
    result = hands.process(rgb_frame)
    return result
