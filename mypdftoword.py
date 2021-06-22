import PyPDF2
import os
import argparse
import docx

"""
parser = argparse.ArgumentParser(description="Pdf to word")

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="pdf to word"
)

args = parser.parse_args() # we save all

"""
document = input('Your pdf: ')


mydoc = docx.Document()

File_path = './'+document
with open (File_path, mode = 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    mydoc.add_paragraph(page.extractText())

mydoc.save("./my_written_file.docx")
