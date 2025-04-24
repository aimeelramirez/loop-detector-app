import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def process_frame(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    loops = 0
    all_landmarks = []

    if result.multi_hand_landmarks:
        hand_bboxes = []
        h, w, _ = frame.shape

        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append({
                    "x": lm.x,
                    "y": lm.y,
                    "z": lm.z
                })
            all_landmarks.append(landmarks)

            x_min = int(min([lm.x for lm in hand_landmarks.landmark]) * w)
            y_min = int(min([lm.y for lm in hand_landmarks.landmark]) * h)
            x_max = int(max([lm.x for lm in hand_landmarks.landmark]) * w)
            y_max = int(max([lm.y for lm in hand_landmarks.landmark]) * h)
            hand_bboxes.append((x_min, y_min, x_max, y_max))

        if len(hand_bboxes) >= 2:
            x1, y1, x2, y2 = hand_bboxes[0]
            x3, y3, x4, y4 = hand_bboxes[1]
            middle_x_min = min(x2, x4)
            middle_x_max = max(x1, x3)
            middle_y_min = min(y1, y3)
            middle_y_max = max(y2, y4)
            middle_region = frame[middle_y_min:middle_y_max, middle_x_min:middle_x_max]

            if middle_region.size > 0:
                loops, _ = detect_loops_and_needles(middle_region)

    return {"hands": all_landmarks, "loops": loops}

def detect_loops_and_needles(needle_region):
    hsv = cv2.cvtColor(needle_region, cv2.COLOR_BGR2HSV)

    # 🎨 White is low saturation, high value
    white_lower = np.array([0, 0, 200])
    white_upper = np.array([180, 40, 255])

    white_mask = cv2.inRange(hsv, white_lower, white_upper)

    kernel = np.ones((3, 3), np.uint8)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)

    white_contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    loop_count = sum(1 for c in white_contours if cv2.contourArea(c) > 50)

    print("⬜ Detected white regions:", loop_count)

    return loop_count, []
