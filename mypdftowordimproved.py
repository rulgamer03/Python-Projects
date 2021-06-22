from pdf2docx import Converter, parse

pdf_file = input("Your pdf: ")
word_file = pdf_file.split(".")[0]+'.docx'
print(word_file)
cv = Converter(pdf_file)
cv.convert(word_file, start=0, end=None)
cv.close()

# parse(pdf_file,word_file, start=0, end=None)
