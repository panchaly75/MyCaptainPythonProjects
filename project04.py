#Write a Python program to print all positive numbers in a range.

print("\tMyCaptain Python project's : 04\t")
print("______________________________________________\n")

ls =[]
counter = int(input("How many integer you want to input : "))

for i in range(0,counter):
	j = int(input(f"Enter a no.{i+1} integer : "))
	ls.append(j)

print("\nPositive Integers are :")
print([ls_positive for ls_positive in ls if ls_positive>0])





#we can also use a normal for loop(above is compress form of +ve_list making statement)
'''
for ls_positive in ls:
	if ls_positive>0:
		print(ls_positive, end=',')
'''

#we can also type cast by float data type in place of int.(in line no. 7 and 10 )

#given i/p is my version type otherwise put i/p manually(in code)
'''
I/p
How many integer you want to input : 5
12
-7
5
64
-14

O/p
[12, 5, 64]
'''
