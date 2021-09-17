from cx_Freeze import setup, Executable

base = None    

executables = [Executable("pdfmanager.py", base=base)]

packages = ["idna","os","PyPDF2","pyttsx3","tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "PdfManager",
    options = options,
    version = "1.0",
    description = 'take it easy',
    executables = executables
)
