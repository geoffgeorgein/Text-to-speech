#Importing the libraries
import cv2
import pytesseract
from PIL import Image

# Specifying the path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# Reading the image
image = cv2.imread('quote2.png')

# Extraction of text from image
text = pytesseract.image_to_string(image)

# Printing the text
print(text)
