import pytesseract
from gtts import gTTS
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(r'ReaderFile.jpg')
language = 'en'

myobj = gTTS(text=text, lang=language, slow=False)

myobj.save("read.mp3")
os.system("read.mp3")