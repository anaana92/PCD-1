import cv2 as cv2
import numpy as np

img = cv2.imread("veis.png")
cv2.imshow("Original Image", img)
kernel = np.ones((3,3),np.uint8)

#erosi
erosion = cv2.erode(img, kernel, iterations = 1)
cv2.imshow("Erosion", erosion)

#dilasi
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("DIlasi", dilation)

#opening
kernel1 = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel1)
cv2.imshow("Opening", opening)

#closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)

#gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel,)
cv2.imshow("Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
