import PyPDF2
import re

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
    
 
# # Write all the files into a file which is named as shown below
output_file_name = "mergetest.pdf"
mergedObject.write(output_file_name)



# Open the pdf file
object = PyPDF2.PdfFileReader(output_file_name)

# Get number of pages
NumPages = object.getNumPages()

# Enter code here
String = "Page break"

page_break_pages = []
# Extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    if re.search(String,Text):
        print("Pattern Found on Page: " + str(i))
        page_break_pages.append(i)
        print(page_break_pages)
