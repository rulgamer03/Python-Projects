# Usa cd para ir a esta direccion
# \Desktop\the-complete-guide-to-bot-creation\batch_renamer
# Now use this line
# python batch_renamer_cli.py document file --filetype .txt --path ./testing


import os
import argparse

parser = argparse.ArgumentParser(description="Batch rename files in directory")
debug = False 
parser.add_argument("search", type=str, help="To be replaced text") # document 
parser.add_argument("replace", type=str, help="Text to use for replacement") # file
parser.add_argument(
    "--filetype",
    type=str, # the extension is a string
    default=None, # We don't have a default value 
    help="Only files with the given type will be renamed (e.g. .txt)"
)
parser.add_argument(
    "--path",
    type=str, # the path is a string
    default=".", # Default value 
    help="Directory path that contains the to be renamed files"
)

args = parser.parse_args() # we save all

# to be replaced string and file extension filter
search = args.search
replace = args.replace
type_filter = args.filetype
path = args.path



print(f"Renaming files at path {path}")

# get all files from current directory
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files.")

# go through all the files and check if they match the search pattern
for doc in docs:
    # separate name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    if debug == True:
        print(f"Debug {doc}")


    # doc -> ./testing\file_27_09_03 - copia (2).txt
    # full_doc_path -> ./testing\file_27_09_03
    # filetype -> .txt
    # doc_path -> ./testing
    # doc_name -> file_27_09_03 - copia (2)

    if debug == True:
        print(f"Debug {full_doc_path} and {filetype}")
    doc_path = os.path.dirname(full_doc_path)
    if debug == True:
        print(f"Debug {doc_path}")
    doc_name = os.path.basename(full_doc_path)
    if debug ==True:
        print(f"Debug {doc_name}")
    # filter for files with the right extension
    if filetype == type_filter or type_filter is None:
        # check if search text is in doc name
        if search in doc_name: 
            #replace with the given text
            new_doc_name = doc_name.replace(search, replace)
            new_doc_path = os.path.join(doc_path, new_doc_name) + filetype
            os.rename(doc, new_doc_path)
            renamed += 1

            print(f"Renamed file {doc} to {new_doc_path}")

print(f"Renamed {renamed} of {len(docs)} files.")
