import cv2

image = cv2.imread('image.jpg')

img = 255 - image

cv2.imshow('Inversion', img)



cv2.waitKey(0)
cv2.destroyAllWindows()