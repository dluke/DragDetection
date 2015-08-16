

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

#cv2.imshow('img',img)
#cv2.imshow('mask',mask)
#cv2.imshow('res',res)


#cv2.waitKey(0)

##cv2.imshow('image',img)
#cv2.destroyAllWindows()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold(gray,127,255,0)

contours,h = cv2.findContours(thresh,1,2)

count = 0
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print len(approx)

    if len(approx)==4:
        count += 1
        print "square"
        cv2.drawContours(img,[cnt],0,(128,255,0),4)
        #cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        #cv2.imshow('img',img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

print 'count', count

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
