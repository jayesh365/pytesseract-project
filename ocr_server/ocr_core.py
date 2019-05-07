# import PIL and PyTesseract
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

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

    # retrun the parsed text
    return parsedText

if __name__ == '__main__':
    print(ocr_core('images/test_one.png'))
    print("")
    print(ocr_core('images/written_test_one.PNG'))
    print("")
    print(ocr_core('images/written_test_two.PNG'))
    print("")
    print(ocr_core('images/written_test_three.PNG'))
    print("")
    print(ocr_core('images/written_test_four.PNG'))
    print("")
    print(ocr_core('images/written_test_five.PNG'))
    print("")
    print(ocr_core('images/test_two.PNG'))

