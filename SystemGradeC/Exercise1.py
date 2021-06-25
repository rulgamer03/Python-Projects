import sys 
import subprocess 
import os 
from os import remove
from os import path

prog = r''' 
#include <stdio.h>
int main() {
  float x =  2.022;
  int y = 20;
  while (x <= y) {
    x = x / 2;
    y = y * x;
  }
  printf("%.2f, %d\n", x, y);
}
'''

answer = input('What is the answer of exercise 1\n')

answer += "\r\n"
answer = bytes(answer, 'ascii')
#print(answer)


if path.exists("foo.exe"):
	remove('foo.exe')
	#print("Remove")


if not os.path.exists('foo'): 
    f = open('foo.c', 'w') 
    f.write(prog) 
    f.close() 
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
