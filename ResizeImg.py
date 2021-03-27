import cv2
import imutils
img = cv2.imread("Python.jpg")
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("resizedImg.jpg",resizeImg)
