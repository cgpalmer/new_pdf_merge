import PyPDF2
import re

# Open the pdf file
object = PyPDF2.PdfFileReader(r"mergetest.pdf")

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
