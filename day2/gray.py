import cv2

image = cv2.imread('image.jpg')

gray = image[:,:,0]*0.3+image[:,:,1]*0.59+image[:,:,2]*0.11

cv2.imshow('Gray', gray)



cv2.waitKey(0)
cv2.destroyAllWindows()