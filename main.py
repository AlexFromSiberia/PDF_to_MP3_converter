from gtts import gTTS
import pdfplumber
from pathlib import Path
from tkinter import *
from tkinter import ttk, filedialog


#GLOBALs
language_of_the_file = 1
path_to_pdf = ''

def txt_to_mp3(text):
    """converts text we have got from the pdf to
     an MP3 file"""
    global language_of_the_file

    if language_of_the_file == 1:
        language = 'ru'
    else:
        language = 'en'
    print(language)
    my_audio = gTTS(text=text, lang=language, slow=False)
    file_name = Path(path_to_pdf).stem
    my_audio.save(f'{file_name}.mp3')
    print (f'[+] {file_name}.mp3 saved')


def pdf_to_txt():
    """convert pdf file to text"""
    global path_to_pdf
    if Path(path_to_pdf).is_file() and Path(path_to_pdf).suffix == '.pdf':
        print(f'File {path_to_pdf} is now converting...Please wait...')
        with pdfplumber.PDF(open(file=path_to_pdf, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        txt_to_mp3(text)

    else:
        print(f'There is no {path_to_pdf} exists. Please check an try again.')


def select_file():
    global path_to_pdf
    path_to_pdf = filedialog.askopenfilename()
    return path_to_pdf


def window():
    """the main window, GUI.
    User have to choose the PDF file and the language of PDF"""
    global path_to_pdf
    global language_of_the_file
    logo = "  ____   ____   _____    _              __  __  ____   _____  \n" \
           " |  _ \ |  _ \ |  ___|  | |_    ___    |  \/  ||  _ \ |___ /  \n" \
           " | |_) || | | || |_     | __|  / _ \   | |\/| || |_) |  |_ \  \n" \
           " |  __/ | |_| ||  _|    | |_  | (_) |  | |  | ||  __/  ___) | \n" \
           " |_|    |____/ |_|       \__|  \___/   |_|  |_||_|    |____/  \n" \
           ""
    root = Tk()
    root.geometry('700x600')
    root.title("PDF  to  MP3")
    root.resizable(height=True, width=True)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    # Lables
    ttk.Label(frm, text=logo, font='Consolas', padding=10).grid(column=0, row=0)
    ttk.Label(text=f'File {path_to_pdf} has been chosen').grid(column=0, row=1)
    # The Radiobutton (select language of the PDF file)
    ttk.Label(frm, text="What is PDF file language?", padding=10).grid(column=0, row=2)
    ttk.Radiobutton(frm, text="Russian", value=1, variable=language_of_the_file, padding=10).grid(column=0, row=3)
    ttk.Radiobutton(frm, text="English", value=2, variable=language_of_the_file, padding=10).grid(column=0, row=4)
    # All the Buttons
    ttk.Button(frm, text="Select the PDF file", command=select_file, padding=10).grid(column=0, row=5)
    ttk.Button(frm, text="Convert a PDF to MP3 file", command=pdf_to_txt, padding=10).grid(column=0, row=6)
    ttk.Button(frm, text="Quit", command=root.destroy, padding=10).grid(column=0, row=7)
    root.mainloop()


if __name__ == '__main__':
    window()

