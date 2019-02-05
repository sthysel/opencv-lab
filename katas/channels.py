#!python

import cv2 as cv

img = cv.imread('../pics/peacock.jpg', cv.IMREAD_COLOR)

yuv_img = cv.cvtColor(img, cv.COLOR_BGR2YUV)
y, u, v = cv.split(img)

cv.imshow('Y channel', y)  # img[:, :, 0]
cv.imshow('U channel', u)  # img[:, :, 1]
cv.imshow('V channel', v)  # img[:, :, 2]

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        exit()
