import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Laranja
    low_orange = np.array([10, 100, 100])
    high_orange = np.array([25, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)

    # Amarelo
    low_yellow = np.array([25, 100, 100])
    high_yellow = np.array([35, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    # Todas as cores menos branco
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

