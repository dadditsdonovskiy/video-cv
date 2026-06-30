import cv2
import numpy as np

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Yellow HSV range
lower_yellow = np.array([20, 80, 80])
upper_yellow = np.array([35, 255, 255])

while True:
    # Read one frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Remove noise
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes
    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)

        cv2.putText(frame, "Yellow", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0,255,0), 2)

    # Display
    cv2.imshow("Webcam", frame)
    cv2.imshow("Mask", mask)

    # Press q to quit
    if cv2.waitKey(1) != -1:
        break
    

cap.release()
cv2.destroyAllWindows()