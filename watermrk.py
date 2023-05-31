from PyPDF2 import PdfFileReader, PdfFileWriter

def create_watermark(input_pdf,output,watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)


        with open(output,'wb') as finalout:
            pdf_writer.write(finalout)

if __name__ == '__main__':
    create_watermark(input_pdf='samplepdf.pdf',output='watermarkedpdf.pdf',watermark='watermark.pdf')