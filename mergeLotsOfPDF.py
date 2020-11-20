from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
# I had 116 files in the folder that had to be merged into a single document
# Loop through all of them and append their pages
# Folder name is in the PDFFilereader(exmaple)
for fileNumber in range(1, 4):
    mergedObject.append(PdfFileReader('6_yuddhakanda_' + str(fileNumber)+ '.pdf', 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write("mergedfilesoutput.pdf")