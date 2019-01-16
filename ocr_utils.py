import pytesseract
import cv2
import os
from PIL import Image


def extract_text(image, thresh=False):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if thresh:
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    tmp_filename = "tmp_%s.png" % os.getpid()
    cv2.imwrite(tmp_filename, gray)
    content = pytesseract.image_to_string(Image.open(tmp_filename))
    os.remove(tmp_filename)

    return content

