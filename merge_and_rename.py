import os
from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()

number_of_pdfs = 0

for file in os.listdir("new/"):
    print(file)
    number_of_pdfs = number_of_pdfs + 1
    print(number_of_pdfs)   
    os.rename(f"new/{file}", f"new/{number_of_pdfs}.pdf")
    mergedObject.append(PdfFileReader("new/" + str(number_of_pdfs) + '.pdf', 'rb'))
    mergedObject.append(PdfFileReader("pb/page_break.pdf", 'rb'))
 
# I had 116 files in the folder that had to be merged into a single document
# Loop through all of them and append their pages
# Folder name is in the PDFFilereader(exmaple)

    
 
# # Write all the files into a file which is named as shown below
mergedObject.write("mergetest.pdf")