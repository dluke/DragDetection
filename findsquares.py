import numpy as np
import cv2

import sys


def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor


image = sys.argv[1]

# Load an color image in grayscale
img = cv2.imread(image)
print img[0][0]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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

mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[big_square_contour],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
mean_val = cv2.mean(img,mask = mask)
html_color = RGBToHTMLColor((mean_val[2],mean_val[1],mean_val[0]))
print html_color


