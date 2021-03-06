#Importing the libraries
import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Specifying the path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# Reading the image
image = cv2.imread('quote2.png')

# Extraction of text from image
text = pytesseract.image_to_string(image)

# Printing the text
print(text)

voice_text = ""

# Converts the text into a single line of text

for i in text.split():
    voice_text += i + ' '

voice_text = voice_text[:-1]
print(voice_text)

tts = gTTS(voice_text)
tts.save("test.mp3")
os.system('test.mp3')
