########## WATERMARKER ##########
##### BORKED DUE TO OUTADET PyPDF2 #####
import PyPDF2

base_file = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()
print(base_file)
print(watermark)

for i in range(len(base_file.pages())):
    page = base_file.getPage(i)
    page.mergePage(watermark.getPage(0))

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)