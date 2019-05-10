import cv2
import numpy as np


def findPage(image):
    filename = image
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    # img[dst > 0.01*dst.max()] = [0, 0, 255]
    img[dst == 205066100.0] = [0, 0, 225]
    img[dst == -54100436.0] = [0, 0, 225]
    print(dst.min(), ",", dst.max())

    cv2.imshow('dst', img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


def locateCheckBoxes(image):
    '''
    (string) -> null
    this function will take in an image of a form, and find all of
    the checkboxes and call locateAnswers()
    '''
    # find countours of a binary image
    # read image
    im = cv2.imread(image)
    # turn to grayscale
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 128, 255, 0)
    # there are 3 params in findContours; src img, countour retrieval mode,
    # contour approximation
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # find all boxes
    for cnt in contours:
        if cv2.contourArea(cnt):
            # draw contour around box
            x, y, w, h = cv2.boundingRect(cnt)
            if x > 995 and w > 35 and h > 14:
                cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 3)
    cv2.imshow('Contour Pic', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def locateAnswers(image):
    '''
    (string) -> null
    this function will traverse all checkboxes and find the answers.
    '''
    im = cv2.imread(image)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 128, 255, 0)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 300:
            # draw contour around box
            x, y, w, h = cv2.boundingRect(cnt)
            if x > 1150 and x < 1460:
                cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 3)
    cv2.imshow('Contour Pic', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    findPage("images/mark.png")
    # locateCheckBoxes("images/dat.png")
