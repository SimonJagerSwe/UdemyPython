########## WATERMARKER ##########
import PyPDF2

base_file = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()
print(base_file)
print(watermark)