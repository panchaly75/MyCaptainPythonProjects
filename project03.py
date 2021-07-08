#Write a Python Program for Fibonacci numbers.

print("\tMyCaptain Python project's : 03\t")
print("______________________________________________\n")
InPut = int(input("How many terms of fibonnaci series want ? : "))

fb= [0, 1]

for i in range(2,InPut):
	fb.append(fb[i-2] + fb[i-1])

print("\n",fb)


"""
I/p
How many terms of fibonnaci series want ? : 13
O/p
0, 1, 1, 2, 3, 5, 8,13, 21, 34, 55, 89, 144,
"""


#if we do'nt want in list data structure, then replace print for loop to given code;
'''
for value in fb:
	print(value, end=',')
'''
