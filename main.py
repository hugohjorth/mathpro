import io
import os

from google.cloud import vision

import cv2

from sympy import *   #Importerar Bibliotek

x, y, z = symbols('x y z')  #Definerar vilka bokstäver som kan användas som variabler
count = ['+', '-', '=']

def removing_noise(imagePath):  #Funktion som gray scalar och blura bilden för att få bättre resultat
    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #Gör bilden grå
    blur = cv2.GaussianBlur(gray, (5,5),0)  #Blurar den
    cv2.imwrite('./images/new.jpg',blur)

def pic_to_text(infile): #Funktion som tar in en bild och returnar texten som står i bilden

    # skapar en client
    client = vision.ImageAnnotatorClient()

    # Öppnar bilden vi väljer som argument till funktionen
    with io.open(infile, 'rb') as image_file:
        content = image_file.read()
  
    image = vision.types.Image(content=content)


    #Använder ocr som text detenction och sparar det i en variabel
    response = client.document_text_detection(image=image)
    #Sparar bara texten vi får tillbaka i en separat variabel
    text = response.full_text_annotation.text

    return text

removing_noise('./images/hugo.jpg')

results = pic_to_text('./images/new.jpg')

#Funktion för att lösa  en ekvation
def cal(thing, variable):
    #skapar ekvationen men replacar "=" tecken med ett "," eftersom biblioteket använder kommat som ett likamed tecken
    main = sympify("Eq(" + thing.replace("=", ",")+")")
    #löser ekvationen men min valda variabel
    answer = solveset(main, variable)
    return answer

#Printar rätt svar
print(cal(results.lower(),x))
