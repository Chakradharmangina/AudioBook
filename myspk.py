from tkinter.filedialog import askopenfilename

import PyPDF2
import pyttsx3
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
speaker = pyttsx3.init()
speaker.setProperty('rate',170)
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[0].id)
page = pdfReader.getPage(1)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()