import argparse
import os
import subprocess

# Open a file for writing and insert some records
with open('exaaaample.tex', 'w', encoding='utf-8') as tex:
  print('''\\documentclass{article}

\\usepackage{xcolor}

\\usepackage{listings}

\\definecolor{mGreen}{rgb}{0,0.6,0}
\\definecolor{mGray}{rgb}{0.5,0.5,0.5}
\\definecolor{mPurple}{rgb}{0.58,0,0.82}
\\definecolor{backgroundColour}{rgb}{0.95,0.95,0.92}
\\author{Angel Raúl Chávez Carrillo}
\\title{C language}
\\lstdefinestyle{CStyle}{
    backgroundcolor=\\color{backgroundColour},   
    commentstyle=\\color{mGreen},
    keywordstyle=\\color{magenta},
    numberstyle=\\tiny\\color{mGray},
    stringstyle=\\color{mPurple},
    basicstyle=\\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    language=C
}

\\lstset{escapeinside={(*@}{@*)}}

\\begin{document}
\\maketitle
\\section{C language}
 A \\textbf{Basic Example}
\\begin{lstlisting}[style=CStyle]
#include <stdio.h>
int main(void)
{
   float x =(*@ \\textcolor{blue}{X}@*);
   int y = Y ;
   while (x <= (*@\\textcolor{blue}{Y}@*)){
        int x = x / (*@\\textcolor{blue}{Z}@*)) ;
        y  = y * x;
   }
   printf("%.2f, %d\n", x, y);
}
\\end{lstlisting}
Some text\\\\
''', file = tex)
  cf = 100
  print( '{\Large \\sc Calificaci\\\'{o}n: %d de 100.}\n\n' % cf, file = tex)
  print('''\\end{document}''', file=tex)


cmd = ['pdflatex', '-interaction', 'nonstopmode', 'exaaaample.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

#retcode = proc.returncode
#if not retcode == 0:
#    os.unlink('cover.pdf')
#    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

# os.unlink('exaaaample.tex')
#os.unlink('exaaaample.log')
