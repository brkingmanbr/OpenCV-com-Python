import cv2
import numpy as np


img = cv2.imread('nissangtr.jpg', cv2.IMREAD_COLOR)
##img[55,55] =[255, 255, 255]
##px = img[55,55]
##print(px)
##ROI = region of interest
roi = img[100:150, 100:150] = [255,255,255]

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
