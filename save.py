import numpy as np
import cv2

import sys

image = sys.argv[1]

# Load an color image in grayscale
img = cv2.imread(image)
print img[0][0]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold(gray,127,255,0)

contours,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

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
M = cv2.moments(big_square_contour)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


print "BIG SQUARE CONTOUR COLOUR BGR"
print img[cx][cy] 

mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[big_square_contour],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
mean_val = cv2.mean(img,mask = mask)


print "pixel points"
print mean_val



#cv2.drawContours(img,[big_square_contour],0,(58,70,183),4)



print 'count', count

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
