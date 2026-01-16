PINCH_THRESHOLD = 0.05  # your tuned value

def detect_pinch(distance, prev_pinched):
    # Correct pinch condition
    is_pinched = distance < PINCH_THRESHOLD

    # ---- Debounce logic ----
    click_event = False

    # Detect transition: NOT pinched -> pinched
    if not prev_pinched and is_pinched:
        click_event = True
        print("CLICK DETECTED")

    return is_pinched, click_event
