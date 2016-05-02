import cv2
import numpy as np

cap = cv2.VideoCapture('foda-se.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('saida.avi', fourcc, 20.0, (640,480))

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)
    
    cv2.imshow('Video',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
out.release()   
cv2.destroyAllWindows()
