import os
import re

import PyPDF2

# set up the email search pattern
email_pattern = r"([a-zA-Z][a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-z]{2,5})" #to obtain a email use https://regex101.com to understand
pattern = re.compile(email_pattern) # to use in a regular expresion

# define the output file
out_file_name = "extract.csv"
out_file = open(out_file_name, "w")
out_file.write("filename, email\n") #write filename and email in the .csv file

# get all pdf files from the current directory
dir_content = os.listdir(".")
pdf_files = [doc for doc in dir_content if doc.endswith("pdf")]
processed = 0

# for each pdf file, read the content and search email
for pdf_file in pdf_files:
    print(f"Extracting email from {pdf_file}...")

    # create a reference to the file and load it using PyPDF2
    pdf_fd = open(pdf_file, "rb") # open this file in the binary format
    pdf_reader = PyPDF2.PdfFileReader(pdf_fd) 

    num_pages = pdf_reader.numPages # number of pages 
    emails = [] # list of emails

    # check all pages for the email
    for page in range(num_pages): # for page in the num_pages
        page_obj = pdf_reader.getPage(page) #page_object

        # get the page text and replace new lines to avoid splitting
        text = page_obj.extractText() # extract the text
        text = text.replace("\n", "") # replace \n by ''

        # search for the email in the text
        email_match = pattern.search(text) # pattern in line 8

        # add the email to the emails list of not present already
        if email_match is not None: # if we found a email
            email = email_match.group()
            if email not in emails:
                emails.append(email)

    if len(emails) == 0:
        print(f"\t=> Email could not be extracted from file {pdf_file}.")

    # close the pdf file descriptor
    pdf_fd.close()

    # write each email in the csv file
    for email in emails:
        out_file.write(f"{pdf_file}, {email}\n") #all in the output file

    processed += 1

out_file.close() # close the out file
print(f"Processed {processed} of {len(pdf_files)} documents")
