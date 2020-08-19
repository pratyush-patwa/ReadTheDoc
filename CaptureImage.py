import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

language = 'en'

playsound("start.mp3")


videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("ReaderFile.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(r'ReaderFile.jpg')
print (text)

try:
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("read.mp3")
    playsound("read.mp3")
except AssertionError:
    playsound("default.mp3")
