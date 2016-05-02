import cv2
import numpy as np

cap = cv2.VideoCapture('foda-se.mp4')
#cap = cv2.imread('nissan-gtr.jpg')

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #HSV = HUE SAT VALUE
    lower_red = np.array([50,0,0])
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
