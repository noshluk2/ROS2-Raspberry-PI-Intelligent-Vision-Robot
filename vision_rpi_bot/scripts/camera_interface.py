import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    # cv2.imshow('frame', gray)
    # if cv2.waitKey(1) == ord('q'):
    #     break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()