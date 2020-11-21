from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("mergetest.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(1))
    output.addPage(inputpdf.getPage(3))
    with open("split_pdfs/largefile-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)