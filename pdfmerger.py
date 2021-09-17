import pyttsx3
import PyPDF2
from tkinter.filedialog import *
def pdfMerger():
    book=askopenfilename()
    pdf_reader=PyPDF2.PdfFileReader(book)
    pdf_file=open('your new pdf.pdf','wb')
    print("enter ur page nos.)
    l=list(map(int,input().split()))
    pdf_writer=PyPDF2.PdfFileWriter()
    for i in l:
       page=pdf_reader.getPage(i)
       pdf_writer.addPage(page)  
       pdf_writer.write(pdf_file)

pdfMerger()    
