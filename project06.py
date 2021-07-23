import csv

def student_detail_in_csv(S_Info):
    with open("Student_Info(2021).csv",'a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Student's Name","Student's Age","Contact No.","Email-ID"])

        writer.writerow(S_Info)

print("\t\t\tMyCaptain Python project's : 06")
print("______________________________________________________________________________\n")
print("Enter a student information in given format\tex: Name,Age,Contact_no.,Email-ID\n")

condition = True
i=1
while condition:

    students_data = input("Enter Student No.{} Info.\t:\t".format(i))
    data2ls = students_data.split(",")

    check_1 = input("\nPlease, Re-check the given Info, Is correct?\n(yes/no)\t:\t")
    if check_1=="yes" or check_1=="Yes":
        student_detail_in_csv(data2ls)
        i += 1

        check_2 = input("\nadd detail of another student(yes/no)\t:\t")
        if check_2 == "yes" or check_2 == "Yes":
            condition = True
        elif check_2 == "no" or check_2 == "No":
            condition = False


    elif check_1=="no" or check_1=="No":
        print("\nRe-Enter the details!\n")

check_3 = input("\nYou want to check student data(yes/no)\t:\t")
if check_3 == "yes" or check_3 == "Yes":
    file_to_open="Student_Info(2021).csv"
    with open(file_to_open, 'r') as this_csv_file:
        this_csv_reader = csv.reader(this_csv_file, delimiter=",")

        for line in this_csv_reader:
            for item in line:
                print(item,end='')
                for i in range(25-len(item)):
                    print(" ",end="")
            print("")


print("\n*******************************************************************************")
print("\t\tThankyou, For adding Info!")
print("*******************************************************************************")

'''
making some changes as MyCaptain app has:
#line : 28-32 ;asking for more data append or not
#line : 38-49 ;to print whole table at last
'''
