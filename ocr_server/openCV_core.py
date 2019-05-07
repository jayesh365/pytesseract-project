import numpy as np 
import cv2

# find countours of a binary image
# read image
im = cv2.imread('images/square.PNG')
# turn to grayscale
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 128, 255, 0)
# there are 3 params in findContours; src img, countour retrieval mode, countour approximation
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[len(contours)-1]
print(cv2.drawContours(im, [cnt], 0, (0,255,0), 3))

cv2.imshow('Contour Pic', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
