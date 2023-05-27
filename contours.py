import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat2.jpg')
cv. imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

# cv.findContours two values based on the edges of the image
# contours is a list of all the coords of contours found in the img
# hierarchies refers to the hierarchical representation of contours, whats inside of what*
# RETER_LIST returns all the contours in the image (diff functions returns different types of contours) 
# cv.CHAIN_APPROX_NONE gives the list of coords of the contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} this many contour(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)