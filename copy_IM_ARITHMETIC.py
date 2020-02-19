import cv2

img1 = cv2.imread('game_of_thrones.jpg', 1)
img2 = cv2.imread('logo.jpg', 1)
rows, columns, channel = img2.shape
roi = img1[0:rows, 0:columns]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 220, 250, cv2.THRESH_BINARY)
cv2.imshow('img2gray', mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:columns] = dst

cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_bg', img2_fg)
cv2.imshow('dst', dst)
cv2.imshow('final', img1)

cv2.namedWindow('final', cv2.WINDOW_GUI_NORMAL)
cv2.waitKey()
cv2.destroyAllWindows()
