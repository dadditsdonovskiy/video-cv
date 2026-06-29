try:
    import cv2
except ImportError:
    print("Error: OpenCV (cv2) is not installed.")
    exit(1)

img = cv2.imread('image.jpg')

if img is None:
    print("Error: Could not read the image.")
    exit()

cv2.imshow('Image', img)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()