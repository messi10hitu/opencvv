import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# to save video we use VideoWriter
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #   HSV = hue sat value

    lower_red = np.array([60, 60, 60])
    upper_red = np.array([180, 255, 255])
    #    lower_red = np.array([0, 0, 0])
    #    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel)  # it just shrinks the pixel
    dilation = cv2.dilate(mask, kernel)  # it widens the pixels
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # opening is the false positive pixel behind the image
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # closing is the false negative pixel on the image

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('erosion', erosion)  # erosion work on every single pixel
    cv2.imshow('dilation', dilation)  # dilation works on the whole are of the pixel
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(1) == 13:
        break

cap.release()
# cap.release()
cv2.destroyAllWindows()
