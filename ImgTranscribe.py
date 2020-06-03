from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\peterson\PycharmProjects\Bots\Tesseract-OCR\Tesseract.exe'
im = Image.open("imagem3.jpg")
text = pytesseract.image_to_string(im, lang='eng')
print(text)




