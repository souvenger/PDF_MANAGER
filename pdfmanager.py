import pyttsx3
import PyPDF2
from PyPDF2 import *
from tkinter import * 
from tkinter import filedialog
import os
def audiobook():
   speaker=pyttsx3.init()
   speaker.say("please ...select the PDF which i will read for u sir")
   speaker.runAndWait() 
   book=filedialog.askopenfilename()
   speaker.say("choose the page no. sir")
   speaker.runAndWait()
   p=int(input("enter page no."))
   pdfReader=PyPDF2.PdfFileReader(book)
   pages=pdfReader.numPages
   speaker.setProperty('rate',130)
   voices=speaker.getProperty('voices')
   speaker.setProperty('voice',voices[0])
   page=pdfReader.getPage(p-1)
   text=page.extractText()
   speaker.say(text)
   speaker.runAndWait()
def pdfsplitter():
    speaker=pyttsx3.init()
    speaker.say("please ...select your file....sir..")
    speaker.runAndWait()
    book=filedialog.askopenfilename()
    pdf_reader=PyPDF2.PdfFileReader(book)
    pdf_file=open('your new pdf.pdf','wb')
    speaker.say("please ...enter your page numbers sir....sir..")
    speaker.runAndWait()
    print("enter ur page nos.")
    l=list(map(int,input().split()))
    pdf_writer=PyPDF2.PdfFileWriter()
    for i in l:
       page=pdf_reader.getPage(i)
       pdf_writer.addPage(page)  
       pdf_writer.write(pdf_file)
def pdfmerger():
    speaker=pyttsx3.init()
    speaker.say("please ...enter the number of PDFs.... u want to enter")
    speaker.runAndWait()
    n=int(input("no.of pdf to merge"))
    pdf=[]
    Pdfwriter=PyPDF2.PdfFileWriter()
    root=Tk()
    root.update()
    root.withdraw()
    speaker=pyttsx3.init()
    speaker.say("please ...select your files....sir..")
    speaker.runAndWait()
    for i in range(n):
        pdf_to_merge=filedialog.askopenfilename()
        root.withdraw()
        root.update()
        pdf.append(pdf_to_merge) 
    for j in pdf:
        pdfReader=PyPDF2.PdfFileReader(open(j,'rb'))
        for page in range(pdfReader.numPages):
            pageobj=pdfReader.getPage(page)
            Pdfwriter.addPage(pageobj)
    pdfoutput=open("new_file"+'.pdf','wb')
    Pdfwriter.write(pdfoutput)
    pdfoutput.close()
    root.destroy()

speak=pyttsx3.init()
speak.say("Hello ..........sir.......    i am your personal PDF manager .........    please say what can i do for u .......  ")
speak.say("choose the corresponding number    for the action   u want to do with your PDF.")
speak.runAndWait()
print("1.Use Audiobook\n2.Use PDF Splitter\n3. Use PDF Merger")
command=int(input())
if command==1:
    speake=pyttsx3.init()
    speake.say("wait sir .......we were opening Audio..book..")
    speake.runAndWait()
    audiobook()
elif command==2:
    speake=pyttsx3.init()
    speake.say("wait sir .......we were opening PDF.. splitter...")
    speake.runAndWait()
    pdfsplitter()
elif command==3:
    speake=pyttsx3.init()
    speake.say("wait sir .......we were opening PDF.....Merger..")
    speake.runAndWait()
    pdfmerger()
else:
    speake=pyttsx3.init()
    speak("please enter valid number")
    speake.runAndWait()
          




  



