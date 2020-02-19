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

    kernel = np.ones((15, 15), np.float32) / 225
    # OpenCV blurs an image by applying what's called a Kernel. A Kernel tells you
    # how to change the value of any given pixel by combining it with different amounts of the neighboring pixels.
    # The kernel is applied to every pixel in the image one-by-one to produce the final image
    # (this operation known as a convolution)
    smoothed = cv2.filter2D(result, -1, kernel)
    blur = cv2.blur(result, (15, 15), 0)
    median = cv2.medianBlur(result, 15)
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
