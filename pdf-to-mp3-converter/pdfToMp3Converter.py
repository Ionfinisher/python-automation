# Here are the packages used to read and convert pdf to mp3:
import pyttsx3
import PyPDF2

source_file_name = ""
output_file_name = ""

pdfReader = PyPDF2.PdfFileReader(open(source_file_name, 'rb'))
speaker = pyttsx3.init()
for pageNumber in range(pdfReader.numPages):
    text = pdfReader.getPage(pageNumber).extractText()
    cleanText = text.strip().replace('\n', ' ')
    speaker.save_to_file(cleanText, output_file_name+".mp3")
    speaker.runAndWait()


speaker.stop()
