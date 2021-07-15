#Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

print("\tMyCaptain Python project's : 05\t")
print("______________________________________________\n")

txt = input("Please enter a string :\t")
op = {ele : txt.count(ele) for ele in list(txt)}                                #compress form of for loop to make dictionary (op), keys are char's and values are char's count
i = len(txt)
while i!=0:                                                                     #sort by decreasing order loop
    for ele in op:
        if op[ele]==i:
            print(ele,"-",op[ele])
    i -= 1


"""
I/p
Please enter a string : Mississippi
O/p
i = 04
s = 04
p = 02
m = 01
"""



"""
#firstly i make this big stuff, to do only one part of code. then search and get replacable one line code.(line : 7)

def most_frequent(st):
    st_list = list(st)
    ele_ls =[]
    count_ls=[]
    final = []

    while len(st_list)!=0:
        for element in st_list:
            count = st_list.count(element)
            print(element,"=",count)
            ele_ls.append(element)
            count_ls.append(count)
            #print(ele_ls, count_ls)

            while st_list.count(element)!=0:
                for i in st_list:
                    if i==element:
                        st_list.remove(element)

txt = input()
most_frequent(txt)
"""
