import random


for i in range(50):
    print("*", end='')
print("")
for j in range(20):
    print("-",end='')
print("Tic-Tac-Toe",end='')
for j in range(20):
    print("-",end='')
print("")
for i in range(50):
    print("*", end='')
print("\n")

condition = True
while condition:
    ls = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


    def cons(pos):
        for j in range(-2, 3):
            for i in range(-2, 3):
                if pos == 1:
                    if j == -2 and i == -2:
                        ls[0][0] = "X"
                elif pos == 2:
                    if j == -2 and i == 0:
                        ls[0][1] = "X"
                elif pos == 3:
                    if j == -2 and i == 2:
                        ls[0][2] = "X"
                elif pos == 4:
                    if j == 0 and i == -2:
                        ls[1][0] = "X"
                elif pos == 5:
                    if j == 0 and i == 0:
                        ls[1][1] = "X"
                elif pos == 6:
                    if j == 0 and i == 2:
                        ls[1][2] = "X"
                elif pos == 7:
                    if j == 2 and i == -2:
                        ls[2][0] = "X"
                elif pos == 8:
                    if j == 2 and i == 0:
                        ls[2][1] = "X"
                elif pos == 9:
                    if j == 2 and i == 2:
                        ls[2][2] = "X"
                else:
                    pass

                if (i == -1 or i == 1) and (j == -1 or j == 1):
                    print("+", end='')
                elif (j == -1 or j == 1):
                    print("--", end='')
                elif (i == -1 or i == 1):
                    print(" |", end='')
                elif (j == -2 and i == -2):
                    print(ls[0][0], end='')
                elif (j == -2 and i == 0):
                    print(ls[0][1], end='')
                elif (j == -2 and i == 2):
                    print(ls[0][2], end='')
                elif (j == 0 and i == -2):
                    print(ls[1][0], end='')
                elif (j == 0 and i == 0):
                    print(ls[1][1], end='')
                elif (j == 0 and i == 2):
                    print(ls[1][2], end='')
                elif (j == 2 and i == -2):
                    print(ls[2][0], end='')
                elif (j == 2 and i == 0):
                    print(ls[2][1], end='')
                elif (j == 2 and i == 2):
                    print(ls[2][2], end='')
            print("")


    def computer_turn():
        print("Computer trun(O):")
        if ls[0][0] == 'O' and ls[0][1] == 'O':  # O_horizontal
            if ls[0][2] == ' ':
                ls[0][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][0] == 'O' and ls[0][2] == 'O':
            if ls[0][1] == ' ':
                ls[0][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][1] == 'O' and ls[0][2] == 'O':
            if ls[0][0] == ' ':
                ls[0][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][0] == 'O' and ls[1][1] == 'O':
            if ls[1][2] == ' ':
                ls[1][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][0] == 'O' and ls[1][2] == 'O':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'O' and ls[1][2] == 'O':
            if ls[1][0] == ' ':
                ls[1][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[2][0] == 'O' and ls[2][1] == 'O':
            if ls[2][2] == ' ':
                ls[2][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[2][0] == 'O' and ls[2][2] == 'O':
            if ls[2][1] == ' ':
                ls[2][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[2][1] == 'O' and ls[2][2] == 'O':
            if ls[2][0] == ' ':
                ls[2][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True

        elif ls[0][0] == 'O' and ls[1][0] == 'O':  # O_vertical
            if ls[2][0] == ' ':
                ls[2][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][0] == 'O' and ls[2][0] == 'O':
            if ls[1][0] == ' ':
                ls[1][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][0] == 'O' and ls[2][0] == 'O':
            if ls[0][0] == ' ':
                ls[0][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][1] == 'O' and ls[1][1] == 'O':
            if ls[2][1] == ' ':
                ls[2][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][1] == 'O' and ls[2][1] == 'O':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'O' and ls[2][1] == 'O':
            if ls[0][1] == ' ':
                ls[0][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'O' and ls[1][2] == 'O':
            if ls[2][2] == ' ':
                ls[2][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'O' and ls[2][2] == 'O':
            if ls[1][2] == ' ':
                ls[1][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][2] == 'O' and ls[2][2] == 'O':
            if ls[0][2] == ' ':
                ls[0][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True

        elif ls[0][0] == 'O' and ls[1][1] == 'O':  # O_cross
            if ls[2][2] == ' ':
                ls[2][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][0] == 'O' and ls[2][2] == 'O':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'O' and ls[2][2] == 'O':
            if ls[0][0] == ' ':
                ls[0][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'O' and ls[1][1] == 'O':
            if ls[2][0] == ' ':
                ls[2][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'O' and ls[2][0] == 'O':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'O' and ls[2][0] == 'O':
            if ls[0][2] == ' ':
                ls[0][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True


        elif ls[0][0] == 'X' and ls[0][1] == 'X':  # X_horizontal
            if ls[0][2] == ' ':
                ls[0][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][0] == 'X' and ls[0][2] == 'X':
            if ls[0][1] == ' ':
                ls[0][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][1] == 'X' and ls[0][2] == 'X':
            if ls[0][0] == ' ':
                ls[0][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][0] == 'X' and ls[1][1] == 'X':
            if ls[1][2] == ' ':
                ls[1][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][0] == 'X' and ls[1][2] == 'X':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'X' and ls[1][2] == 'X':
            if ls[1][0] == ' ':
                ls[1][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[2][0] == 'X' and ls[2][1] == 'X':
            if ls[2][2] == ' ':
                ls[2][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[2][0] == 'X' and ls[2][2] == 'X':
            if ls[2][1] == ' ':
                ls[2][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[2][1] == 'X' and ls[2][2] == 'X':
            if ls[2][0] == ' ':
                ls[2][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True

        elif ls[0][0] == 'X' and ls[1][0] == 'X':  # X_vertical
            if ls[2][0] == ' ':
                ls[2][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][0] == 'X' and ls[2][0] == 'X':
            if ls[1][0] == ' ':
                ls[1][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][0] == 'X' and ls[2][0] == 'X':
            if ls[0][0] == ' ':
                ls[0][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][1] == 'X' and ls[1][1] == 'X':
            if ls[2][1] == ' ':
                ls[2][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][1] == 'X' and ls[2][1] == 'X':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'X' and ls[2][1] == 'X':
            if ls[0][1] == ' ':
                ls[0][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'X' and ls[1][2] == 'X':
            if ls[2][2] == ' ':
                ls[2][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'X' and ls[2][2] == 'X':
            if ls[1][2] == ' ':
                ls[1][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][2] == 'X' and ls[2][2] == 'X':
            if ls[0][2] == ' ':
                ls[0][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True

        elif ls[0][0] == 'X' and ls[1][1] == 'X':  # X_cross
            if ls[2][2] == ' ':
                ls[2][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][0] == 'X' and ls[2][2] == 'X':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'X' and ls[2][2] == 'X':
            if ls[0][0] == ' ':
                ls[0][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'X' and ls[1][1] == 'X':
            if ls[2][0] == ' ':
                ls[2][0] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[0][2] == 'X' and ls[2][0] == 'X':
            if ls[1][1] == ' ':
                ls[1][1] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True
        elif ls[1][1] == 'X' and ls[2][0] == 'X':
            if ls[0][2] == ' ':
                ls[0][2] = 'O'
            else:
                check = True
                while check:
                    a = random.randrange(3)
                    b = random.randrange(3)
                    if ls[a][b] == " ":
                        ls[a][b] = "O"
                        check = False
                    else:
                        check = True


        else:
            check = True
            while check:
                a = random.randrange(3)
                b = random.randrange(3)
                if ls[a][b] == " ":
                    ls[a][b] = "O"
                    check = False
                else:
                    check = True

        for j in range(-2, 3):
            for i in range(-2, 3):
                if (i == -1 or i == 1) and (j == -1 or j == 1):
                    print("+", end='')
                elif (j == -1 or j == 1):
                    print("--", end='')
                elif (i == -1 or i == 1):
                    print(" |", end='')
                elif (j == -2 and i == -2):
                    print(ls[0][0], end='')
                elif (j == -2 and i == 0):
                    print(ls[0][1], end='')
                elif (j == -2 and i == 2):
                    print(ls[0][2], end='')
                elif (j == 0 and i == -2):
                    print(ls[1][0], end='')
                elif (j == 0 and i == 0):
                    print(ls[1][1], end='')
                elif (j == 0 and i == 2):
                    print(ls[1][2], end='')
                elif (j == 2 and i == -2):
                    print(ls[2][0], end='')
                elif (j == 2 and i == 0):
                    print(ls[2][1], end='')
                elif (j == 2 and i == 2):
                    print(ls[2][2], end='')
            print("")


    def check():
        for opt in ['X', 'O']:
            for k0 in range(3):
                if ls[k0][0] == opt and ls[k0][1] == opt and ls[k0][2] == opt:
                    print("\n--------------------------------------------------------------\n\t\t", opt,
                          "player is Winner!")
                    return False
                elif ls[0][k0] == opt and ls[1][k0] == opt and ls[2][k0] == opt:
                    print("\n--------------------------------------------------------------\n\t\t", opt,
                          "player is Winner!")
                    return False
                elif ls[0][0] == opt and ls[1][1] == opt and ls[2][2] == opt:
                    print("\n--------------------------------------------------------------\n\t\t", opt,
                          "player is Winner!")
                    return False
                elif ls[2][0] == opt and ls[1][1] == opt and ls[0][2] == opt:
                    print("\n--------------------------------------------------------------\n\t\t", opt,
                          "player is Winner!")
                    return False

        for k1 in range(3):
            for k2 in range(3):
                if ls[k1][k2] == ' ':
                    return True
        return False


    run = True
    print("Position type \n1\t2\t3\n4\t5\t6\n7\t8\t9\nyou must type 'X' character as your side")
    while run:
        try:
            print("Player turn(X) :")
            position = input("\t\tEnter a position : ")
            cons(int(position))
            run = check()
            if run == True:
                computer_turn()
                run = check()
        except ValueError:
            print("\n--------------------------------------------------------------\n\t\tMatch is Draw")
            break


    check0 = input("\n\n\n\n\nYou want to play again?\n(yes/no)\t:\t")
    if check0 == "yes" or check0 == "Yes" or check0 == "YES" or check0 == "y" or check0 =="Y": condition = True
    else: condition = False
