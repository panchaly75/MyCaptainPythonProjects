############################################___OOP's : Object Oriented___###############################################

'''
#define Class
by keyword 'class' we make class,
after this keyword, name the class what ever you want(but must be discriptive,as variable define)
after that applied ':' and press 'enter', for entering into the class
'''
class student_data0():
    print("Into the class")


'''
#__init__()
called as Constructor method/intialize method/dunder methods (because they begin and end with double underscores)
its a primary method, generally used for making multiple objects
first parameter should be 'self',for signify its all values for class(included its functions,etc.)
into the class, we generally call functions as methods.(for more clarification) 

> self.age = age creates an attribute called age and assigns to it the value of the age parameter.
> Use class attributes to define properties that should have the same value for every class instance.  {Eg. collage} 
> Use instance attributes for properties that vary from one instance to another.  {Eg. name,branch,etc.,}
'''
class student_data1():
    collage = "SGSITS, Indore"
    def __init__(self, name, branch, year, enroll):
        self.name = name
        self.branch = branch
        self.year = year
        self.enroll = enroll



# if we instantiate a class without storing into variable(object), it shows as location of object
print(student_data0())
#if we storing into variables, both the objects are differ
student1 = student_data0()
student2 = student_data0()
print(student1==student2)
'''
if their are required some parameter,then it through error {Eg. student1 = student_data1()
                                                                student2 = student_data1()
                                                                print(student1==student2)
'''



#we can access their instance attributes using dot notation
student1 = student_data1("Yash Panchal","Biomedical Engg.","B.Tech. IIIyr.","0801BM191067")
print(student1.enroll)



'''
method definning into the class, and using of that 
'''
class student_data2():
    collage = "SGSITS, Indore"
    def __init__(self, name, branch, year, enroll):
        self.name = name
        self.branch = branch
        self.year = year
        self.enroll = enroll

    def info(self):
        print(f"{self.name}\n{self.collage}\n{self.branch}\n{self.year}\n{self.enroll}")

std1 = student_data2("Amaan Khan","Biomedical Engg.","B.Tech. IIIyr.","0801BM191007")
print(std1.info())



'''
Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, 
and the classes that child classes are derived from are called parent classes.
> Child classes can override or extend the attributes and methods of parent classes
'''
class student_data3():
    collage = "SGSITS, Indore"
    def __init__(self, name, branch, year, enroll):
        self.name = name
        self.branch = branch
        self.year = year
        self.enroll = enroll

    def info(self, collage):
        print(f"{self.name}\n{collage}\n{self.branch}\n{self.year}\n{self.enroll}")

std1 = student_data3("Amaan Khan","Biomedical Engg.","B.Tech. IIIyr.","0801BM191007")
print(std1.info("DAVV, Indore"))




















'''
Points to remember:
> Define a class, which is a sort of blueprint for an object
> Instantiate an object from a class
> Use attributes and methods to define the properties and behaviors of an object
> Use inheritance to create child classes from a parent class
> Reference a method on a parent class using super()
> Check if an object inherits from another class using isinstance()
'''