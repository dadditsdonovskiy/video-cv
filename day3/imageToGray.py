import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError("Could not load image.")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("image_gray.jpg", gray)

# Display the grayscale image
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()