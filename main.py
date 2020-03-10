import io
import os

from google.cloud import vision

import cv2

from sympy import *

x, y, z = symbols('x y z')
count = ['+', '-', '=']

def removing_noise(imagePath):
    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    cv2.imwrite('./images/new.jpg',blur)

def pic_to_text(infile):
    """Detects text in an image file

    ARGS
    infile: path to image file

    RETURNS
    String of text detected in image
    """

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Opens the input image file
    with io.open(infile, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # For dense text, use document_text_detection
    # For less dense text, use text_detection
    response = client.document_text_detection(image=image)
    text = response.full_text_annotation.text

    return text

removing_noise('./images/hugo.jpg')

results = pic_to_text('./images/new.jpg')
print(results)

# for i in results:
#     if not i.isdigit():
#         if not i in count:
#             pass

def cal(thing, variable):
    main = sympify("Eq(" + thing.replace("=", ",")+")")
    answer = solveset(main, variable)
    return answer

print(cal(results.lower(),x))