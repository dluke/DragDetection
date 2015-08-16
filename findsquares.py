import numpy as np
import cv2
import json
import random
import numpy as np

import sys


# RGB for JSON #

def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor

# random location generator for JSON #

def random_lattitutde_generator():
    top = 55.95493
    bot = 55.89530
    yrange = np.linspace(bot, top, 10000)

    left = -3.14166
    right = -3.33735
    xxrange = np.linspace(right, left, 10000)

    count = 1
    while True:
        y = random.sample(yrange, 1)[0]
        x = random.sample(xxrange, 1)[0]
        yield (x, y), count
        count = count + 1

coordinate_gen = random_lattitutde_generator()


# opencv fun #

image = sys.argv[1]

# Load a color image in grayscale
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
        cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

print "count"
print count
sorted_squares = sorted(squares, key=lambda k: k['area'])
big_square_contour = sorted_squares[-2]['contour']

mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[big_square_contour],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
mean_val = cv2.mean(img,mask = mask)

# consolidating data into a JSON #
html_color = RGBToHTMLColor((mean_val[2],mean_val[1],mean_val[0]))
(lon,lat),count= coordinate_gen.next()
dic = {u'id':count,u'color':html_color, u'latitude':lat,u'longitude':lon}
output_filename = 'data' + str(count) + '.json'


with open(output_filename, 'w') as outfile:
    json.dumps(dic)

