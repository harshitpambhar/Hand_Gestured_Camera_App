import cv2

def open_camera():
    cap = cv2.VideoCapture(0)

    # Check if camera opened
    if not cap.isOpened():
        print("❌ Camera not opened")
        exit()

    print("✅ Camera opened")
    return cap
