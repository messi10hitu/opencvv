import cv2
import numpy as np

'''
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
'''
cap = cv2.VideoCapture(0)
# to save video we use VideoWriter
# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # FourCC is a 4-byte code used to specify the video codec.
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) == 13:
        break

cap.release()
# cap.release()
cv2.destroyAllWindows()
