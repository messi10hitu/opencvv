import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi.jpg', 1)
#                 (area)            (B,G,R)    (line width)

# Create a black image
# img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (150, 150), (0, 0, 0), 15)

#                    |            300(___)200
#                   (x1,y1)     (x2, y2)
cv2.rectangle(img, (15, 25), (300, 200), (255, 0, 0), 5)  # for rect we need top-left and botom-right corner of rect
#                 (centre) , (radius=193), (color), (thickness)
cv2.circle(img, (430, 290), 193, (0, 0, 255), 10)
cv2.rectangle(img, (1475, 250), (1625, 450), (255, 255, 255), 10)
pts = np.array([[175, 150], [120, 130], [170, 120], [150, 100], [125, 160]], np.int32)  # here pts is point of polynmial
cv2.polylines(img, [pts], True, (0, 255, 255), 5)  # here True means that 1st cordinate will connect to the last

# -------------write on image---------------
font = cv2.FONT_HERSHEY_SIMPLEX
# it starts from=(100, 500) , have font, spacing B/W lines = 3, color, thickness=5
cv2.putText(img, "Messi10Hitu", (100, 700), font, 3, (0, 0, 0), 5)

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # use to minimize the size of windows
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Messi shoots the ball')
plt.show()
'''
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('IMG_0140.JPG', 0)
px = img[100, 100]
print(px)
cv2.line(img, (0, 0), (150, 150), (0, 0, 0), 15)
cv2.rectangle(img, (15, 25), (300, 200), (255, 255, 255), 15)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
'''
