# Here are the packages used to read and convert pdf to mp3:
import pyttsx3
import PyPDF2


pdfReader = PyPDF2.PdfFileReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()
for pageNumber in range(pdfReader.numPages):
    text = pdfReader.getPage(pageNumber).extractText()
    cleanText = text.strip().replace('\n', ' ')
    speaker.save_to_file(cleanText, 'story.mp3')
    speaker.runAndWait()


speaker.stop()
