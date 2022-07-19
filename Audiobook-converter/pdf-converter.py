from PyPDF2 import PdfReader


def pdf_converter():
    reader = PdfReader("/home/nico/Desktop/sample.pdf")
    page = reader.pages[0]
    return page.extract_text()
    


print(pdf_converter())