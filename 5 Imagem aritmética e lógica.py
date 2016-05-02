import cv2
import numpy as np

#Soma de imagens:
#As duas imagens são 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

add = img1+img2
#add = cv2.add(img1,img2) soma o BGR de cada pixel

cv2.imshow('add',add)
cv2.waitKey(0)
##cv2.destroyAllWindows()

#Soma com peso:
#                          img param img param e gamma
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) 
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
##cv2.destroyAllWindows()

#Sobrepondo imagem

img1 = cv2.imread('3D-Matplotlib.png',cv2.IMREAD_COLOR)
img2 = cv2.imread('mainlogo.png')
# ERRO:          print(img1.shape)

# ROI = Region of Interest
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Mascara inversa da logo
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# threshold = limiar limite
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# apagar a área do logo na area de interesse
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Pegar apenas a região do logo na imagem
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
