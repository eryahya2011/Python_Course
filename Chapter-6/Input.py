# Input Function In Python 

# a = input("1")
# print(int(a)+int(a))

# Input Function read as a String Always.

name = input("Enter Your Name: ")
print(f"Welcome {name} to the Python Programme.")

age = input("Enter Your Age: ")
print(f"Next Year You Will Turn {int(age)+1} !")


# Multiple Inputs:

x = input("Enter First Number: ")
y = input("Enter Second Number:")
print(f"The Sum Of Both The numbers {x} and {y} is {int(x) + int(y)}")


# Home Work: Write a program to input student name marks in 3 subjects and print name and percentage of the student.

Student_Name = input("Enter Student Name: ")
Mathematics = input("Enter Marks in Mathematics: ")
Science = input("Enter Marks in Science: ")
English = input("Enter Marks in English: ")
print(f"{Student_Name} has got {Mathematics}, {Science}, and {English} Respectively.")
print(f"Percentage of {Student_Name} is {((int(Mathematics) + int(Science) + int(English))/300)*100}%")