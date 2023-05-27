from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=0, help="max buffer size")
args = vars(ap.parse_args())

# upper and lower boundaries of the color of the tennis ball
# list of the previous tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

# use webcam if video path is not supplied
if not args.get("video", False):
    vs = VideoStream(src=0).start()
# grab reference to the video file otherwise 
else:
    vs=cv2.VideoCapture(args["video"])

# let camera turn on/warm up
time.sleep(5.0)

# loops through all the frams
while True:
    # get the current frame
    frame = vs.read()

    # choose to get from stream or capture
    frame = frame[1] if args.get("video", False) else frame

    # end if there are no more frames
    if frame is None:
        break

    # resize the frame, blur it, and convert it to HSV
    frame = imutils.resize(frame, width = 600)
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


        if radius > 15:
            cv2.circle(frame, (int(x), int(y)), int(radius), (34,139,34), 2)
            cv2.circle(frame, center, 5, (0,0,255), -1)

    pts.appendleft(center)

    for i in range(1, len(pts)):

        if pts[i - 1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (255, 0 ,0), thickness)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if (key == ord("q")):
        break

if not args.get("video", False):
    vs.stop()
else:
    vs.release()

cv2.destroyAllWindows()



