########## PDFs ##########
import PyPDF2
import sys

'''
with open('dummy.pdf', 'rb') as file:
    # print(file)
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    print(reader.pages[0])
    page = reader.pages[0]
    print(page)
    page.rotate(90)

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
'''
    

# Merging exercise
input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(input)