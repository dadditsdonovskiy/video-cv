import cv2
import numpy as np

image = cv2.imread('image.jpg')

h,w,_ = image.shape
for i in range(0,h,10):
    for j in range(0,w,10):
        image[i:i+5,j:j+5] = np.random.randint(0,255,3)

cv2.imshow('Glitch', image)



cv2.waitKey(0)
cv2.destroyAllWindows()