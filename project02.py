#write a python program to accept a filename from the user and print the extension of that.

print("\tMyCaptain Python project's : 02\t")
print("______________________________________________\n")

file_name = input("The Filename : ")

if '.py' in file_name :
	print("The extension of the file is : 'python'")
elif '.cpp' in file_name :
	print("The extension of the file is : 'C++ language'")
elif '.c' in file_name :
	print("The extension of the file is : 'C language'")
elif '.java' in file_name :
	print("The extension of the file is : 'Java'")
elif '.html' in file_name :
	print("The extension of the file is : 'HTML'")
elif '.pdf' in file_name :
	print("The extension of the file is : 'portable document format'")
elif '.doc' in file_name :
	print("The extension of the file is : 'document'")
else :
	print("This formate is not define!")

#we make it much longer by using different formates

"""
I/p
The Filename : abc.py
O/p
The extension of the file is : 'python'
"""