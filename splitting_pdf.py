from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_Split(path,name_of_split):
    pdf_reader = PdfFileReader(path)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))

        with open(f'{name_of_split}{page}.pdf','wb')as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
    path='samplepdf.pdf'
    pdf_Split(path,'pdfPage')