import cv2
img = cv2.imread("OpenCV.png")
cv2.imshow("OpenCV",img)
cv2.imwrite("Sample.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
