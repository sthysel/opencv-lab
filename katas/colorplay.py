#!python

import cv2 as cv

SCALE = 2.0


def help():
    print("""
        Change color space of the
        input video stream using keyboard controls. The control keys are:
            g: Grayscale
            y: YUV
            h: HSV
    """)


if __name__ == '__main__':
    help()
    cap = cv.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    cur_mode = None
    while True:
        # Read the current frame from webcam
        ret, frame = cap.read()

        # Resize the captured image
        frame = cv.resize(
            frame,
            None,
            fx=SCALE,
            fy=SCALE,
            interpolation=cv.INTER_AREA,
        )

        c = cv.waitKey(1)
        if c == 27:
            break
        # Update cur_mode only in case it is different and key was pressed
        # In case a key was not pressed during the iteration result is -1 or 255, depending
        # on library versions
        if c != -1 and c != 255 and c != cur_mode:
            cur_mode = c

        if cur_mode == ord('g'):
            output = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        elif cur_mode == ord('y'):
            output = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
        elif cur_mode == ord('h'):
            output = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        else:
            output = frame
        cv.imshow('Webcam', output)

    cap.release()
    cv.destroyAllWindows()
