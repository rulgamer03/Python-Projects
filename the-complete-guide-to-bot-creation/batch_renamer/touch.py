# python touch.py --c 4 documento{0..20}.java
# python touch.py --c 3 delete{5..10}.py
# python touch.py --c 1 demo{2..9}.c
# python touch.py --c 2 homework{1..5}.docx
# python touch.py --c 2 --path ./testing example{1..3}.xls
import os
import argparse

def makeonefile(path, file):
	with open(os.path.join(path, file), 'w') as fp:
		pass 



def makefiles(path_here,b, a, name, ext, digit): # 0 100 document .txt 3 
	# print(digit)
	# print(len(str(a)))
	if digit >= len(str(a)):
		for i in range(b,a+1):
			namefile = c+str(i).zfill(digit)+"."+ext
			print(namefile)
			makeonefile(path_here, namefile)
	else:
		print("Is not possible")




# ---------------------------------------------------------------------------------------------


parser = argparse.ArgumentParser(description="Create files name001 names002 etc.")

parser.add_argument(
    "--c",
    type=int, # the number of digits are int
    default=3, # Default value 
    help="Number of digits"
)


parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of the to be cleaned up directory"
)


parser.add_argument("line", type=str, help="Document{a.b}.ext") # Line

args = parser.parse_args() # we save all
linetowork = args.line
digits = args.c
path_input = args.path

# print(digits)
# print(linetowork)

# documento{0..100}.tex
numberofpoints = linetowork.count('.')
if numberofpoints == 3 and digits > 0:
	extension=linetowork.split(".")[3]
	# print(extension)
	a = linetowork.split(".")[2]
	a = a.strip("}")
	b = linetowork.split(".")[0]
	c = b.split("{")[0]
	b = b.split("{")[1]
	a = int(a)
	b = int(b)
	# extension = txt
	# a -> 100
	# b -> 0
	# c -> documento 
	# print(a)
	# print(b)
	# print(c)
	if a > b and a > 0 and b >= 0 and len(c)>0 and len(extension)>0: # all values correct
		makefiles(path_input ,b, a, c, extension, digits)
	else:
		print("Is not possible")

