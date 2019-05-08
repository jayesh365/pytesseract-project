# import PIL and PyTesseract
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from openCV_core import locateCheckBoxes


def ocr_core(imgPath):
    '''
    (string) -> string
    This function will take in an image at <imgPath> and
    attempt to parse the text in the image.
    '''
    # initialize variable to represent the parsed text
    # Pillow will be used to open the image, and PyTesseract
    # will be used to parse strings from the image
    parsedText = pytesseract.image_to_string(Image.open(imgPath))
    parsedTextD = pytesseract.image_to_data(Image.open(imgPath))
    print(parsedTextD)
    # parsedTextLocation = pytesseract.image_to_boxes(Image.open(imgPath))
    # put all parsed text into an array
    parsedTextArr = [i for i in parsedText]
    print(parsedTextArr)

    # traverse the parsed text to find the special char to start openCV
    for j in range(len(parsedTextArr)):
        if parsedTextArr[j] == 'x' and parsedTextArr[j-1] == 'x':
            locateCheckBoxes(imgPath)
    return parsedText


if __name__ == '__main__':
    ocr_core('images/check.PNG')
