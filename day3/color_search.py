import cv2

import numpy as np



# Read image
img = cv2.imread("image.jpg")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Red has two hue ranges in HSV
lower_red1 = np.array([0, 100, 80])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 100, 80])
upper_red2 = np.array([180, 255, 255])

# Create masks
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# HSV range for light blue
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# HSV range for light green (mint)
lower_green = np.array([45, 30, 80])
upper_green = np.array([90, 255, 255])

lower_yellow = np.array([20, 80, 80])
upper_yellow = np.array([35, 255, 255])

# Create mask
maskGreen = cv2.inRange(hsv, lower_green, upper_green)

maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)

maskYellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

mask = maskYellow
# Apply mask
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("Blue Object", result)
cv2.waitKey(0)
cv2.destroyAllWindows()