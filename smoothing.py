import cv2 as cv

img = cv.imread('Photos/lady.jpg')
cv.imshow('Cat', img)

# Averaging 
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gauss', gauss)

# Median 
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

# Bilateral, retains edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)