import numpy as np
import cv2
import json
import random
import numpy as np
import sys


# RGB HTML hex color converter #

def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '%02x%02x%02x' % rgb_tuple
    # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor

def generate_samples(mean_val):
    html_color = RGBToHTMLColor((mean_val[2],mean_val[1],mean_val[0]))
    (lon,lat)= coordinate_gen.next()
    random_id = random.sample(xrange(100000),1)[0]
    dic = {u'id':str(random_id),u'value':str(html_color), u'latitude':str(lat),u'longitude':str(lon)}
    return dic


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
        yield (x, y)

# initilaise random location generator

coordinate_gen = random_lattitutde_generator()


# opencv fun #
# We get the contours and look for squares. 
# We use the 2nd largest square as
# the frame was detected as well for some reason.

image = sys.argv[1]

# Load a color image in grayscale
img = cv2.imread(image)

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

sorted_squares = sorted(squares, key=lambda k: k['area'])
big_square_contour = sorted_squares[-2]['contour']

mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[big_square_contour],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
mean_val = cv2.mean(img,mask = mask)

# Generating test samples with random locations:
# adhering to Joey's JSON format requirements

random_id = random.sample(xrange(100000),1)[0]
obj = open('test'+ str(random_id) + '.json','wb')
obj.write('[')
for i in xrange(100):
    dic = generate_samples(mean_val)
    obj.write(json.dumps(dic))
    obj.write(',')
obj.write(']')
obj.close

