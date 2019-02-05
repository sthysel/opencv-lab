import numpy as np
import cv2
import time
import cv2.cv as cv

cap = cv.VideoCapture(0)
time.sleep(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if frame is None:
        print('ef')
        continue

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
