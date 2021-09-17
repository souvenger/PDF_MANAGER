import pyttsx3
import PyPDF2
from PyPDF2 import *
from tkinter import * 
from tkinter import filedialog
import os
def pdfmerger():
    n=int(input("no.of pdf to merge"))
    pdf=[]
    Pdfwriter=PyPDF2.PdfFileWriter()
    root=Tk()
    root.update()
    root.withdraw()
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
pdfmerger()    
