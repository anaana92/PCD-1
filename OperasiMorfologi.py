import cv2 as cv2
import numpy as np

img = cv2.imread("veis.png")
cv2.imshow("Original Image", img)
kernel = np.ones((3,3),np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel,)
cv2.imshow("Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()