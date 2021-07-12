'''
Q1_In w3schools:
    - List
    - Tuple
    - Set
    - Dictionary
    - String
    - If-else
    - Loops
'''


#List : [], mutable, ordered, duplication allow
ls = ["yash", "MyCaptain", "Python"]                                            #construct list
print(ls)
ls = list(("C++","C"))
print(ls)

print(type(ls))                                                                 #type of list

print(len(ls))                                                                  #lenght of list

ls0 = []                                                                        #empty list
print(ls0)

ls1 = [32, True,  45.737, "yash", 'a']                                          #store any type of data
print(ls1)

print(ls[0])                                                                    #access by indexing
print(ls1[-2])                                                                  #access by -ve index ( 0 to n : -n to -1)
print(ls1[1:3:2])                                                               #slicing (start:stop:step), if empty [::] means [0:n:1]

ls1[3] = "Gowtham"                                                              #update
print(ls1)
ls1.append("yash")                                                              #add at last
print(ls1)
ls1.insert(3,"chitranshi")                                                      #add at given index
print(ls1)
ls1.extend(ls)                                                                  #extend a list
print("ls :",ls)
print("xtend_ls1 :",ls1)

ls1.remove("C")                                                                 #remove
print(ls1)
ls1.pop(3)                                                                      #pop(), use index default last element
print(ls1)
del ls1[3]                                                                      #same as pop()
print(ls1)
ls1.clear()                                                                     #clear all elements
print(ls1)




#Tuple : (), immutable, ordered, duplication allow
tp = ("yash", "MyCaptain", "Python")                                            #construct tuple
print(tp)
tp = tuple(("C++","C"))
print(tp)

print(type(tp))                                                                 #type of tuple

print(len(tp))                                                                  #lenght of tuple

tp0 = ("yash",)                                                                 #make a single element tuple by adding comma in last otherwise it store as string
print(type(tp0), tp0)

tp1 = (32, True,  45.737, 32, "yash", 'a', 32)                                  #store any type of data
print(tp1)

print(tp[0])                                                                    #access by indexing
print(tp1[-2])                                                                  #access by -ve index ( 0 to n : -n to -1)
print(tp1[1:3:2])                                                               #slicing (start:stop:step), if empty [::] means [0:n:1]

print(tp1.count(32))                                                            #count a given value in tuple
print(tp1.index("yash"))                                                         #locate given value in form of index

                                                                                #if we want to update or doing mutable operation, so it became gave error because tuples are immutable.



#Set : {}, mutable, unordered, unchangeable, duplication not allow(automatic make to single)
s = {"yash", "MyCaptain", "Python"}                                             #construct set
print(s)
s = set(("C++","C"))
print(s)

print(type(s))                                                                  #type of set

print(len(s))                                                                   #lenght of set

s0 = {}                                                                         #empty set
print(s0)

s1 = {32, True,  45.737, "yash", 'a'}                                           #store any type of data
print(s1)

print('a' in s1)                                                                #to check present or not

s1.add("chiku")                                                                 #for adding value i.e.,mutablity
print(s1)
s.update(s1)                                                                    #adding one set values to another
print("s :",s)
print("s1 :",s1)

s.remove("C")                                                                   #remove, if element not avail it through error
print(s)
s.discard("C")                                                                  #sort error through thing
print(s)
s.pop()                                                                         #pop(), only index because unordered
print(s)
del s1                                                                          #delete whole set completely
s.clear()                                                                       #clear all elements
print(s)

s2 = {2, "a", 3, "b"}
s3 = {1, 2, 3, 4}
print(s2.union(s3))                                                             #give union of 2 sets
print(s2.intersection(s3))                                                      #give intersection of 2 sets
print(s2.symmetric_difference(s3))                                              #opposite to intersection
print(s2.isdisjoint(s3))                                                        #return two sets have a intersection or not
print(s2.issubset(s3))                                                          #a set contain this set or not
print(s2.issuperset(s3))                                                        #a set contain another set or not




#Dictionary : {key:value}, mutable, ordered, changeable
dict = {"yash" : "student", "MyCaptain" : "App", "Python" : "language"}         #construct dictionary
print(dict)

print(dict["yash"])                                                             #access by indexing key
print(dict.get("yash"))                                                         #same as above(method; later discused)

print(dict.keys())                                                              #give all keys present in dict
print(dict.values())                                                            #give all values present in dict
print(dict.items())                                                             #give all key-value pairs

print(type(dict))                                                               #type of dictionary

print(len(dict))                                                                #lenght of dict

dict["collage"] = "SGSITS"                                                      #add new key-value
print(dict)
dict["Python"] = "programming language"                                         #updating value
print(dict)

dict1 = {"age" : 32, "vote": True, "percent": 45.737}                           #store any type of data
print(dict1)

dict1.pop("vote")                                                               #pop(),erase key-value
print(dict1)
del dict1["percent"]                                                            #delete key-value, and also whole
print(dict1)
dict1.clear()                                                                   #clear all elements
print(dict1)

dict2 = dict.copy()                                                             #make a copy of given dict
print("dict2 :",dict2)

n_dict = {"yash":{"age":20, "vote":True}, "chiku":{"age":14, "vote":False}}     #nested dictionary
print(n_dict)




#String :
st = "hello yash!"                                                              #string uses double quotes, three times double quotes, three times single quotes
print(st)

print(st[3])                                                                    #access element of string by indexing
print(st[2:9:2])                                                                #slicing also possible

print(len(st))                                                                  #length of String

print(st.upper())                                                               #upper casing
print(st.lower())                                                               #lower casing

print(st.replace("h","A"))                                                      #replacing element or word
print(st.split(" "))                                                            #split a string by given character

st2 = " how are you?"
print(st + st2)                                                                 #string concatenation

age = 20
st3 = "my age is {}"
print(st3.format(age))                                                          #using by variable without type cast

print("t\nt")                                                                   #new line
print("t\tg")                                                                   #tab

                                                                                #many other methods avail on yhis link "https://www.w3schools.com/python/python_strings_methods.asp"


#If-else :
i = True
if i:                                                                           #if-else in simple
    print(i)
else:
    print(not i)

i = 6
if i<0:                                                                         #if-else nested
    if i<-10:
        print("less than -10")
    else:
        print("more than -10 and less than 0")
else:
    if i<10:
        print("less than 10 and more than 0")
    else:
        print("more than 10")

i = 4
if i==1:                                                                        #elif ladder
    print("its 1")
elif i==2:
    print("its 2")
elif i==3:
    print("its 3")
elif i==4:
    print("its 4")
elif i==5:
    print("its 5")
                                                                                #only main is this, other than it only operators and keywords




#Loops : while loop, for Loops
counter = 0                                                                     #while loop : (intialize, condition, increment)
while counter<10:
    print(counter+1)
    counter += 1


for i in range(10):                                                             #for loop : (use only keywords, that's why looking easy than while)
    print(i+1)                                                                  #keywords which generally used are (in, is, etc.) which is just similer to english language

print(i+1 for i in range(10))                                                   #contract form of loop                                            
