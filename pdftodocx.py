from pdf2docx import Converter

pdf_file = 'resume.pdf'
docx_file = 'output/resume.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
#output file is saved as 'output/resume.docx'