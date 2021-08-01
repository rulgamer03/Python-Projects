import random

def make_matrix(m,t,n=0):
    for i in range(t):
        m.append([])
        for j in range(t):
            m[i].append(n)

def print_matrix(m,t):
    character = "#"
    print(f"|  ", end="  | ")
    for j in range(t):
        print (f"{j+1:3d}", end="  ")
    print()
    print("-"*t*5+"-"*5)
    for i in range(t):
        print(f"| {letters[i]}", end="  | ")
        for j in range(t):
            print (f"{m[i][j]:3d}", end="  ")
        print()
    print("-"*t*5+"-"*5)
    print()

def put_mines(m,t,n_mines):
    i = 0
    while(i < n_mines):
        a = random.randint(0, t-1) # genera un número entero entre a y b, ambos incluidos
        b = random.randint(0, t-1) # genera un número entero entre a y b, ambos incluidos)
        if (m[a][b]!=-1):
            m[a][b]=-1
            i+=1


def count_mines(m,t):
    count = 0
    for i in range(t):
        for  j in range(t):
            if (m[i][j]==-1):
                count+=1
    return(count)


def count_neighboring_mines(m,i,j,t):
    c = 0
    for x in range((i-1),(i-1+3)):
        for y in range ((j-1),(3+j-1)):
            if (x>=0 and y >= 0 and x < t and y < t):
                if (m[x][y]==-1):
                    c+=1
    return c




def put_numbers(m,t):
    for i in range(t):
        for  j in range(t):
            if (m[i][j]!=-1):
                m[i][j]=count_neighboring_mines(m,i,j,t)

def print_while_playing(m,d,t):
    character = "#"
    print(f"|  ", end="  | ")
    for j in range(t):
        print (f"{j+1:3d}", end="  ")
    print()
    print("-"*t*5+"-"*5)
    for i in range(t):
        print(f"| {letters[i]}", end="  | ")
        for j in range(t):
            if (d[i][j]==0):
                print(f"  {character}", end="  ")
            else:
                print (f"{m[i][j]:3d}", end="  ")
        print()
    print("-"*t*5+"-"*5)
    print()

def discover(m,d,t,a,b):
    if (m[a][b]==-1): # is a mine
        return -1 # You lose
    elif(d[a][b]==1):
        return 0 # already discovered
    else: # we have something that is not a mine
        if (m[a][b]==0):
            d[a][b]=1 # we discover a 0
            for x in range((a-1),(a-1+3)):
                for y in range ((b-1),(3+b-1)):
                    if (x>=0 and y >= 0 and x < t and y < t):
                        discover(m,d,t,x,y)
        else:
            d[a][b]=1 # we discover a n!=0


def win(d,t,n_mines):
    c = 0
    for i in range(t):
        for  j in range(t):
            if (d[i][j]==1):
                c+=1
    if (c==t*t-n_mines):
        return 1 # You win
    else:
        return 0 # Keep playing

play = True
answer = "Y"
letters =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letters_dic = {}
for i in range(1,27):
    letters_dic.update({letters[i-1]:i})

# print(letters_dic)
# print(letters_dic["A"])
while (play==True):
    tam = 0
    number_of_mines = 0
    lose = False
    wining = False
    answer = input("\nDo you want to play? Y/N \n")
    if (answer=="Y" or answer=="y"):
        while (tam < 3 or tam > 26):
            tam = int(input("\nWrite the size of the matrix (Number from 3 to 26)\n"))
            
        max_number_mines = int(tam*tam*0.75)
        while (number_of_mines < 1 or number_of_mines > max_number_mines):
            number_of_mines = int(input(f"\nWrite the number of mines (Number from 1 to {max_number_mines}) \n"))
        matrix = []
        discovered  = []
        make_matrix(matrix,tam)
        make_matrix(discovered ,tam)
        # print_matrix(matrix,tam)
        # print_matrix(discovered ,tam)
        put_mines(matrix,tam,number_of_mines) # put_mines(m,t,n_mines):
        # print_matrix(matrix ,tam)
        # print(count_mines(matrix,tam))
        put_numbers(matrix,tam)
        # print_matrix(matrix ,tam) # ! To cheat
        print_while_playing(matrix,discovered,tam)
        while (lose==False and wining==False ):
            letter_a = input(f"write the row (Letter from A to {letters[tam-1]}) ")
            try:
                letter_a = letter_a.upper()
            except:
                letter_a = "ABCD123"    
            
            while (letter_a not in letters[0:tam]):
                letter_a = input(f"write the row (Letter from A to {letters[tam-1]}) ")
                try:
                    letter_a = letter_a.upper()
                except:
                    letter_a = "ABCD123"

            
            a = letters_dic[letter_a.upper()]
            a-=1

            b = int(input(f"write the column (Number from 1 to {tam}) "))
            while (b<1 or b>tam):
                b = int(input(f"write the row (Number from 1 to {tam}) "))
            b-=1

            if (matrix[a][b]==-1):
                print("\nYou lose, You touch a mine\n")
                print_matrix(matrix ,tam)
                lose = True
            else:
                discover(matrix,discovered,tam,a,b)
                if (win(discovered,tam,number_of_mines)):
                    print("\nCongratulations You win\n")
                    wining = True
                print()
                print_while_playing(matrix,discovered,tam)
                
    elif (answer=="N" or answer=="n"):
        print("\nHave a nice day\n")
        play=False
    else:
        print("\nPlease write Y or N \n")
