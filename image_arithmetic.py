import cv2
import numpy as np
import matplotlib.pyplot as plt

# img1 = cv2.imread('game_of_thrones.jpg', 1)
# img2 = cv2.imread('logo.jpg', 1)

# add = img1 + img2
# add = cv2.add(img1, img2)
# cv2.imshow('add', add)

# weight shows the percentage of image her img1%=0.8
# weighted = cv2.addWeighted(img1, 0.8, img2, 0.5, 0)
# cv2.imshow('add', weighted)

# Bitwise operation
# Load two images
img1 = cv2.imread('game_of_thrones.jpg', 1)
img2 = cv2.imread('logo.jpg', 1)
# I want to put logo on top-le
# ft corner, So I create a ROI = Region Of Intrest
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
# here the mask is the black part
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# thresholding converts gray-scale image into a binary image
# where the two levels are assigned to pixel that are below or above the specific threshold value
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('img2gray_mask', mask)


# now we will pick only the logo and forget the mask from original image
# create its inverse mask
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI, we use 2 roi bcoz it will give us regio of intrest in img1
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

# Take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst


cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_fg', img1_bg)
cv2.imshow('img2_bg', img2_fg)
cv2.imshow('dst', dst)
cv2.imshow('final', img1)

cv2.namedWindow('final', cv2.WINDOW_GUI_NORMAL)
cv2.waitKey()
cv2.destroyAllWindows()
