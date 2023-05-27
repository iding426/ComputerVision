import cv2 as cv

bos = cv.imread('Photos/boston.jpg')

img = cv.resize(bos, (int(bos.shape[1] * .5), int(bos.shape[0] * .5)), interpolation=cv.INTER_AREA)
cv.imshow('Boston', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB, displays reverse because opencv reads in BGR instead of RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RBG', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv -> bgr', hsv_bgr)

cv.waitKey(0)