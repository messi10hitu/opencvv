import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi.jpg', 1)
px = img[500, 750]
img[500, 750] = [255, 255, 255]

# ROI ==> region of intrest

img[250:500, 250:750] = [255, 0, 0]
cv2.rectangle(img, (250, 500), (750, 800), (255, 0, 0), 10)

ball = img[950:800, 1100:875]
img[450:300, 500:275] = ball
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # use to make our window responsive
# cv2.imwrite('messi_gray.jpg', img)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
