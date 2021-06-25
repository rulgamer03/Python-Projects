import sys 
import subprocess 
import os 
from os import remove
from os import path
import random


B = 3

answer = input('What is the answer of exercise 2\n')
line = "log(a)/log(BASE)+1" # line that you know that works fine


comprobations = 10
A = [] # A is any non negative number
for i in range(comprobations):
    aux = random.randrange(20)
    if aux is not A:
        A.append(aux)


corrects = 0

for i in range(comprobations):
    with open(f'foo.c', 'w', encoding='utf-8') as tex:
        print("""
        #include <stdio.h>
        #include <math.h>
        #define BASE %d
        int main() {
            int a = %d;
        """ %(B, A[i]), file=tex)
        print("""
            int d = %s;
        """ % line, file=tex)
        print("""
            printf("%d needs %d digits in base %d\\n", a, d, BASE);
        }
        """, file=tex)

    with open(f'fooyouranswer.c', 'w', encoding='utf-8') as tex2:
        print("""
        #include <stdio.h>
        #include <math.h>
        #define BASE %d
        int main() {
            int a = %d;
        """ %(B, A[i]), file=tex2)
        print("""
            int d = %s;
        """ % answer, file=tex2)
        print("""
            printf("%d needs %d digits in base %d\\n", a, d, BASE);
        }
        """, file=tex2)


    remove('foo.exe')

    remove("fooyouranswer.exe")

    subprocess.call(["gcc", "foo.c", "-ofoo", "-std=c99", '-w', '-Ofast'])

    subprocess.call(["gcc", "fooyouranswer.c", "-ofooyouranswer", "-std=c99", '-w', '-Ofast'])

    try:
        cmd = subprocess.Popen('./fooyouranswer', stdout=subprocess.PIPE)
        cmd_out, cmd_err = cmd.communicate()
        print(cmd_out)

    except:
        print("Error the C file created by the student don't compile")
        break


    try:
        cmd2 = subprocess.Popen('./foo', stdout=subprocess.PIPE)
        cmd_out2, cmd_err2 = cmd2.communicate()
        print(cmd_out2)

    except:
        print("Error the C file created by the teacher don't compile")
        break

    if cmd_out2 == cmd_out:
        corrects+=1


if corrects == comprobations:
    print("All correct")
else:
    print("Sometimes or Always incorrect")






"""
answer = input('What is the answer of exercise 1\n')

answer += "\r\n"
answer = bytes(answer, 'ascii')
#print(answer)


if path.exists("foo.exe"):
	remove('foo.exe')
	#print("Remove")


if not os.path.exists('foo'):
    subprocess.call(["gcc", "foo.c", "-ofoo", "-std=c99", '-w', '-Ofast']) 



try:
	# subprocess.call(["./foo"], stdin = sys.stdin)
	cmd = subprocess.Popen('./foo', stdout=subprocess.PIPE)
	cmd_out, cmd_err = cmd.communicate()
	#print(cmd_out)
	#print(cmd_err)
	#print(cmd_out == answer)

except:
	print("Error the C file don't compile")

if cmd_out == answer:
    print("Correct answer")
else:
    print("Incorrect answer")
"""
