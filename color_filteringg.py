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
    result = cv2.bitwise_and(frame, frame, mask=mask)  # this result is the mixture of frames and mask
    final_result = cv2.resize(result, (300, 300))
    final_mask = cv2.resize(mask, (300, 300))
    final_frame = cv2.resize(frame, (300, 300))

    cv2.imshow('frame', final_frame)
    cv2.imshow('mask', final_mask)
    cv2.imshow('final_result', final_result)

    if cv2.waitKey(1) == 13:
        break

cap.release()
# cap.release()
cv2.destroyAllWindows()
