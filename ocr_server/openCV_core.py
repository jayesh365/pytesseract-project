import numpy as np 
import cv2

def locateCheckBoxes(image):
    '''
    this function will take in an image of a form, and find all of the checkboxes.
    '''
    # find countours of a binary image
    # read image
    im = cv2.imread(image)
    # turn to grayscale
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 128, 255, 0)
    # there are 3 params in findContours; src img, countour retrieval mode, countour approximation
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(im, contours, -1, (0,255,0), 3)
    # find all boxes
    for cnt in contours:
        if cv2.contourArea(cnt) < 1000 and cv2.contourArea(cnt) > 500:
            # draw contour around box
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0),3)

    # open window to show results
    cv2.imshow('Contour Pic', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
