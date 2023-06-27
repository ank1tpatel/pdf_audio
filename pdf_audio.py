import pyttsx3, PyPDF2

#read pdf file
pdfreader = PyPDF2.PdfReader(open('Principles of Mangerial Economics - Chapter 3.pdf','rb'))
reader = pyttsx3.init()
for page in range(len(reader.pages)):
    text = pdfreader.getPage(page).extractText()
    legible_text = text.strip().replace('\n',' ')
    print(legible_text)
    reader.say(legible_text)
    reader.save_to_file(legible_text,'file.mp3')
    reader.runAndWait()
reader.stop()