#!python

import cv2 as cv

img = cv.imread('../pics/peacock.jpg', cv.IMREAD_COLOR)
g, b, r = cv.split(img)

ggr_img = cv.merge((g, g, r))
rbr_img = cv.merge((r, b, r))

cv.imshow('Original', img)
cv.imshow('GRB', ggr_img)
cv.imshow('RBR', rbr_img)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        exit()
