#Ques 3

SID =int(input("Enter the SID :"))
print("SID",SID)
Name =(input("Enter your name :"))
print("Your Name", Name)
Gender=(input("enter student Gender :"))
print("Student Gender :",Gender)
Course=(input("Student course name:"))
print("Studentvcourse",Course)
CGPA=float(input("Enter Student CGPA:"))
print("Student CGPA",CGPA)
Student =[]
Student.append(SID)
Student.append(Name)
Student.append(Gender)
Student.append(Course)
Student.append(CGPA)
print(Student)