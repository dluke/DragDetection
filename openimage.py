
help  = 'run this with an image as first argument'


import numpy as np
import cv2

import sys

image = sys.argv[1]

# Load an color image in grayscale
img = cv2.imread(image)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 60, 50])
upper_red = np.array([180, 255, 200])

mask = cv2.inRange(hsv, lower_red, upper_red)

res = cv2.bitwise_and(img,img, mask= mask)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.namedWindow('res', cv2.WINDOW_NORMAL)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)


#cv2.imshow('image',img)
cv2.destroyAllWindows()
