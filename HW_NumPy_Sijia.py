import numpy as np
import random


#get information from player
print("Welcome to play two-dimensional Tic-Tac-Toe!")

print()

priority = int(input("If you want to go first please type 1, if not please type 2: "))

print()

square = np.zeros((3,3), dtype=str)


#Create function
def check_row_win(index):
    num = 0
    n = 0
    for x in square[index]:
        if x == 'X':
            num += 1
        elif x == 'O':
            n += 1
    return num,n

        
def check_col_win(index):
    amt = 0
    a = 0
    for x in square[:,index]:
        if x == 'X':
            amt += 1
        elif x == 'O':
            a += 1
    return amt,a

def determine_winner():
    #Check row to find winer
    num1,n1 = check_row_win(0)
    num2,n2 = check_row_win(1)
    num3,n3 = check_row_win(2)

    #Check column to find winer
    amt1,a1 = check_col_win(0)
    amt2,a2 = check_col_win(1)
    amt3,a3 = check_col_win(2)
    
    if num1 == 3 or num2 == 3 or num3 == 3:
        print("You win!")
        win = False
    elif n1 == 3 or n2 == 3 or n3 == 3:
        print("Computer win!")
        win = False

    elif amt1 == 3 or amt2 == 3 or amt3 == 3:
        print("You win!")
        win = False
    elif a1 == 3 or a2 == 3 or a3 == 3:
        print("Computer win!")
        win = False
                       
    elif square[0,0] == 'X' and square[1,1] == 'X' and square[2,2] == 'X':
        print("You win!")
        win = False

    elif square[0,2] == 'X' and square[1,1] == 'X' and square[2,0] == 'X':
        print("You win!")
        win = False

    elif square[0,0] == 'O' and square[1,1] == 'O' and square[2,2] == 'O':
        print("Conputer win!")
        win = False

    elif square[0,2] == 'O' and square[1,1] == 'O' and square[2,0] == 'O':
        print("Conputer win!")
        win = False

    else:
        print("It’s a draw.")
        print()
        win = True


#if player go first 
if priority == 1:
    win = True  
    while win:
        row,col = input("Please entry your indicate by a pair of numbers (e.g. first row and first column: '0 0'): ").split()
        print()
        row = int(row)
        col = int(col)
        
        square[row,col] = 'X'
        print(square)

        #Check row to find winer
        num1,n1 = check_row_win(0)
        num2,n2 = check_row_win(1)
        num3,n3 = check_row_win(2)

        #Check column to find winer
        amt1,a1 = check_col_win(0)
        amt2,a2 = check_col_win(1)
        amt3,a3 = check_col_win(2)
            
        if num1 == 3 or num2 == 3 or num3 == 3:
            print("You win!")
            break
        
        elif amt1 == 3 or amt2 == 3 or amt3 == 3:
            print("You win!")
            break
                       
        #Check diagonal to find winer
        elif square[0,0] == 'X' and square[1,1] == 'X' and square[2,2] == 'X':
            print("You win!")
            break

        elif square[0,2] == 'X' and square[1,1] == 'X' and square[2,0] == 'X':
            print("You win!")
            break

        else:
            print("It’s a draw.")
            print()


        #computer step
        print("Computer step:")
        com = True
        while com:
            c_row = random.randint(0,2)
            c_col = random.randint(0,2)

            if c_row != row and c_col != col:
                if square[c_row,c_col] != 'O' and square[c_row,c_col] != 'X':
                    square[c_row,c_col] = 'O'
                    com = False
        print(square)
        print()

        determine_winner()

                
#computer go first
elif priority == 2:
    win = True
    while win:
        print("Computer step:")
        com = True
        while com:
            c_row = random.randint(0,2)
            c_col = random.randint(0,2)

            if square[c_row,c_col] != 'O' and square[c_row,c_col] != 'X':
                square[c_row,c_col] = 'O'
                com = False
        print(square)
        print()
            
        #Check row to find winer
        num1,n1 = check_row_win(0)
        num2,n2 = check_row_win(1)
        num3,n3 = check_row_win(2)

        #Check column to find winer
        amt1,a1 = check_col_win(0)
        amt2,a2 = check_col_win(1)
        amt3,a3 = check_col_win(2)
            

        if n1 == 3 or n2 == 3 or n3 == 3:
            print("Computer win!")
            break

        elif a1 == 3 or a2 == 3 or a3 == 3:
            print("Computer win!")
            break

                                       
        #Check diagonal to find winer
        elif square[0,0] == 'O' and square[1,1] == 'O' and square[2,2] == 'O':
            print("Conputer win!")
            break

        elif square[0,2] == 'O' and square[1,1] == 'O' and square[2,0] == 'O':
            print("Conputer win!")
            break

        else:
            print("It’s a draw.")
            print()
                
            
        #player entry
        row,col = input("Please entry your indicate by a pair of numbers (e.g. first row and first column: '0 0'): ").split()
        print()
        row = int(row)
        col = int(col)
        square[row,col] = 'X'
        
        print(square)
        print()

        determine_winner()
 





