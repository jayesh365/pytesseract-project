import cv2
# import ocr_core


def locateCheckBoxes(image):
    '''
    this function will take in an image of a form, and find all of
    the checkboxes.
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
    # cv2.drawContours(im, contours, -1, (0,255,0), 3)
    # find all boxes
    # cnt = 581
    for cnt in contours:
        if cv2.contourArea(cnt) > 382 and cv2.contourArea(cnt) < 1079:
            # draw contour around box
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 3)
            print(x, y, w, h)
    # find the answers
    locateAnswers(image)


def locateAnswers(image):
    im = cv2.imread(image)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 128, 255, 0)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) < 300:
            # draw contour around box
            x, y, w, h = cv2.boundingRect(cnt)
            if x > 1150 and y >= 4 and x < 1450:
                cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 3)
    cv2.imshow('Contour Pic', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
