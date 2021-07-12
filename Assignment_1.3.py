#Q3_Create a Calculator.


opt = 1                                                                         #for each operation define a function
def addition(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def pwr(a, b):
    return a**b

def reminder(a, b):
    return a%b

def Fdivision(a, b):
    return a//b

def And():                                                                      #not take float value so take i/p in function and disply
    x = int(input("Enter a 1st no.: "))
    y = int(input("Enter a 2nd no.: "))
    print(x&y)

def Or():
    x = int(input("Enter a 1st no.: "))
    y = int(input("Enter a 2nd no.: "))
    print(x|y)

def Xor():
    x = int(input("Enter a 1st no.: "))
    y = int(input("Enter a 2nd no.: "))
    print(x^y7)

print("\t\t\t\tMyCaptain Python Assignment : 1.3")
print("____________________________________________________________\n")

while (opt==1):                                                                 #loop which sort re-run problem
    print("----------------------BASIC-CALCULATOR----------------------\n")
    print(
        "Choose any one option \n1.\tADDITION\n2.\tSUBTRACT\n3.\tMULTIPLICATION\n4.\tDIVISION\n5.\tREMINDER\n6.\tFLOOR DIVISION\n7.\tPOWER\n8.\tAND (BitWise)\n9.\tOR (BitWise)\n10.\tXOR (BitWise)\n")
    i = int(input(""))
    if i<8 and i>0:
        x = float(input("Enter a 1st no.: "))
        y = float(input("Enter a 2nd no.: "))

    if (i == 1):
        print(addition(x, y))
    elif (i == 2):
        print(subtract(x, y))
    elif (i == 3):
        print(multiply(x, y))
    elif (i == 4):
        print(divide(x, y))
    elif (i == 5):
        print(reminder(x, y))
    elif (i == 6):
        print(Fdivision(x, y))
    elif (i == 7):
        print(pwr(x, y))
    elif (i == 8): And()
    elif (i == 9): Or()
    elif (i == 10): Xor()
    else:
        print("invalide!!!")

    opt = int(input("do you want to exit\n1. no\n2. yes\n\t"))

print("\n\tThankyou for visiting!\n\n")
