from PyPDF2 import PdfFileReader

path = "pb/page_break.pdf"
with open(path, 'rb') as f:
    pdf = PdfFileReader(f)
    info = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    
    print(info)
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
    name = info.name

    print(author)
    print(name)