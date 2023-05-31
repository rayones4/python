import PyPDF2
a = PyPDF2.PdfFileReader('progit.pdf')
print(a.documentInfo)
print(a.getNumPages())
for i in range(1, 11):

    str += a.getPage(2).extractText()