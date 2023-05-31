import PyPDF2
a = PyPDF2.PdfFileReader('samplepdf.pdf')
print(a.documentInfo)
print(a.getNumPages())