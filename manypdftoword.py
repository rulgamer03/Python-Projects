from pdf2docx import Converter, parse
import os


# get all json files from current directory
dir_content = os.listdir(".")
pdf_files = [doc for doc in dir_content if doc.endswith("pdf")]
#processed = 0
#pdf_file = input("Your pdf: ")
#word_file = pdf_file.split(".")[0]+'.docx'
#print(word_file)

lista = []
for pdf_file in pdf_files:
	word_file = pdf_file.split(".")[0]+'.docx'
	try:
		cv = Converter(pdf_file)
		cv.convert(word_file, start=0, end=None)
		cv.close()
		lista.append(f"{pdf_file} to {word_file} success\n")
	except:
		lista.append(f"{pdf_file} to {word_file} failed\n")


print() # A white line
# parse(pdf_file,word_file, start=0, end=None)
for line in lista:
	print(line)
