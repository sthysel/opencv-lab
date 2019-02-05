#!python

from pprint import pprint
import cv2 as cv

conversions = [x for x in dir(cv) if x.startswith('COLOR_')]
pprint(conversions)

img = cv.imread('../pics/peacock.jpg', cv.IMREAD_COLOR)
cv.imshow('Peacock', img)
cv.waitKey()

for c in conversions:
    try:
        name = 'Converted Window'
        _c = getattr(cv, c)
        converted = cv.cvtColor(img, _c)
        cv.imshow(name, img)
        cv.waitKey()
    except cv.error:
        cv.destroyWindow(name)
        print(f'{c} not valid for this conversion')

cv.destroyAllWindows()
