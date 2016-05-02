import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('nissangtr.jpg', cv2.IMREAD_GRAYSCALE)
#Outras opções:
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1

cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("resultado.png",img)
##plt.imshow(img, cmap='gray', interpolation='bicubic')
##plt.plot([50,100],[80,200], 'c', linewidth=5)
##plt.show()
