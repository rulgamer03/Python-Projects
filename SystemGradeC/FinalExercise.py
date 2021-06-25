import sys 
import subprocess 
import os 
from os import remove
from os import path

prog = r''' 
#include <stdio.h>
#define READ 01
#define WRITE 02
#define EXECUTE 04
typedef enum {FALSE = 0, TRUE = 1} boolean;
int main(int x, char* y[]) {
  int i;
  for (i = 1; i < x; i++) {
    unsigned int status = 0;
    char* pos = y[i];
    boolean done = FALSE;
    while (!done) {
      switch (pos[0]) {
      case '\0':
        done = TRUE;
        break;
      case 'r':
        status |= READ;
        break;
      case 'w':
        status |= WRITE;
        break;
      case 'x':
        status |= EXECUTE;
        break;
      default:
        break;
      }
      pos++;
    }
    printf("%d ", status);
  }
  printf("\n");
}
'''

answer = input('What is the answer of the last exercise\n')

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
    cmd = subprocess.Popen('./foo ' + answer, stdout=subprocess.PIPE)
    cmd_out, cmd_err = cmd.communicate()
    print(cmd_out)
    #print(cmd_err)
    #print(cmd_out == answer)

except:
    print("Error the C file don't compile")

if cmd_out == b'1 4 6 \r\n':
    print("Correct answer")
else:
    print("Incorrect answer")
