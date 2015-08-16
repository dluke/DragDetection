import numpy as np
import cv2

import sys

image = sys.argv[1]

# Load an color image in grayscale
img = cv2.imread(image)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold(gray,127,255,0)

contours,h = cv2.findContours(thresh,1,2)

squares = []
count = 0
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
    area = cv2.contourArea(cnt)

    if len(approx)==4 and (area > 10000):
        squares.append({'area': area, 'contour':cnt})
        count = count + 1

sorted_squares = sorted(squares, key=lambda k: k['area'])
big_square_contour = sorted_squares[-2]['contour']
cv2.drawContours(img,[big_square_contour],0,(128,255,0),4)


print 'count', count

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
