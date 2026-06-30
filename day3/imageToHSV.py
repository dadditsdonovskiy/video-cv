import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError("Could not load image.")

# Convert from BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Save the HSV image (optional)
cv2.imwrite("image_hsv.png", hsv)

# Display the original and HSV images
cv2.imshow("Original", image)
cv2.imshow("HSV", hsv)

h, s, v = cv2.split(hsv)

cv2.imshow("Hue", h)
cv2.imshow("Saturation", s)
cv2.imshow("Value", v)


flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

cv2.waitKey(0)
cv2.destroyAllWindows()