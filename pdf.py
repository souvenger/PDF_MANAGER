import pyttsx3
import PyPDF2
from tkinter.filedialog import *
#file=input("enter ur file")
p=int(input("enter page no."))
book=askopenfilename()
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
speaker=pyttsx3.init()
speaker.setProperty('rate',130)
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[0])
page=pdfReader.getPage(p)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
