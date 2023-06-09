import cv2 as cv

# img = cv.imread('Photos/cat1.jpeg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    #works for images, videos, and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    diminsions = (width, height)
    

    return cv.resize(frame, diminsions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# capture = cv.VideoCapture('Videos/dog.mp4')

def changeRes(width, height):
    #only works for live video (webcams)
    capture.set(3, width)
    capture.set(4, height)

#reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = .2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()