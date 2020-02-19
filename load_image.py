import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IMG_0140.JPG', 0)
# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_COLOR = 1
# cv2.IMREAD_UNCHANGED = -1

'''# showing image using cv2 and opencv shows (B.G.R)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# if we want to save the image in our directory 
cv2.imwrite('IMG_0140.png', img)
'''

# showing image using matplot and it shows (R.G.B)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([300, 700], [650, 700], 'r', linewidth=5)
#         [x1,  y1], [x2,   y2], color = "red"
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
