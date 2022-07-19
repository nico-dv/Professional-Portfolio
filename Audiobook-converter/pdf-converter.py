"""" This converts a pdf into a string"""

import PyPDF2

pdfFileObject = open("/home/nico/Desktop/nicolae-valeanu.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

print(" No. Of Pages :", pdfReader.numPages)

pageObject = pdfReader.getPage(0)

# pageObject.extract_text()

