# OOPs In Python:

#OOPs stands for object oriented programming system.  

# You need to create a class first to create an object.
# Class is a blueprint of an object. It has its own attributes and methods.

#                           Class
#                             |
#                     ------------------
#                     |                |
#                   Attribute        Method
#                     |                |
#                     ------------------
#                              |
#                           Object


# Using list - Create student records:
# Student Details:

student_1 = ['Madhav', 10]
student_2 = ['Vishaka', 12]

print(f'{student_1[0]} is in class {student_1[1]}')

# This is not a good way to represent the student details. And not practically possible for a huge data.
# This is when we feel need of OOPs.

# Using OOPs - Create student records:

# Class - Blueprint.
class Student:   # Student Class 
    def __init__(self, name, grade, percentage):  # Method
        self.name = name  # Attribute
        self.grade = grade  # Attribute
        self.percentage = percentage  # Attribute
    
    def student_details(self): # Method
        print(f'{self.name} is in class {self.grade} with {self.percentage}%')
# Object - instance of a class
student_1 = Student('Yahya', 11, 96)
print(student_1.name, student_1.grade, student_1.percentage)

student_1.student_details()

print(student_1.__dict__)  # To see the attributes of the object in a dictionary format.


# Modify Object Property/Attribute:
Student.percentage = 98  # Modifying the percentage.
print(student_1.percentage)  # This will not change the percentage of student_1

# Delete Object Property/Attribute:
del student_1.percentage  # Deleting the percentage attribute of student_1
print(student_1.__dict__)  # To see the attributes of the object in a dictionary

# Delete Object:
del student_1  # Deleting the student_1 object
# print(student_1)  # This will give an error as student_1 is deleted.




# Class - Blueprint.
class Student:   # Student Class 
    def __init__(self, name, grade, percentage, team):  # Method
        self.name = name  # Attribute
        self.grade = grade  # Attribute
        self.percentage = percentage  # Attribute
        self.team = team  # Attribute
    
    def student_details(self): # Method
        print(f'{self.name} is in class {self.grade} with {self.percentage}% and is in team {self.team}')

team1 = 'A'
team2 = 'B'

# Object - instance of a class
student_1 = Student('Yahya', 11, 96, team1)
student_2 = Student('Vishaka', 10, 92, team2)
print(student_1.name, student_1.grade, student_1.percentage)
print(student_2.name, student_2.grade, student_2.percentage)

# student_1.student_details()
# student_2.student_details()
print(student_1.team)
print(student_2.team)
 



# Feautres In OOPs :

# There are 4 features in OOPs;
# 1.  Abstraction
# 2.  Encapsulation
# 3.  Inheritence 
# 4.  Polymorphism

# 1. Abstraction :- It hides unnecessary details from users through class & methods. 

class Student:   # Student Class 
    def __init__(self, name, grade, percentage):  # Method
        self.name = name  # Attribute
        self.grade = grade  # Attribute
        self.percentage = percentage  # Attribute
    
    def student_details(self): # Method - abstraction
        print(f'{self.name} is in class {self.grade} with {self.percentage+2}%')  # Hidden From Users
# Object - instance of a class
student_1 = Student('Yahya', 11, 96)
student_2 = Student('Vishaka', 10, 92)

student_1.student_details()


# Encapsulation :-  Restrict action on certain attributes oor methods to protect data and enforce controlled access.

class Student:   # Student Class 
    def __init__(self, name, grade, percentage):  # Method
        self.name = name  # Attribute
        self.grade = grade  # Attribute
        self.__percentage = percentage  # Double Underscore limits access
    
    def get_percentage(self):
        return self.__percentage

    def student_details(self): # Method 
        print(f'{self.name} is in class {self.grade} with {self.percentage}%') 
# Object - instance of a class
student_1 = Student('Yahya', 11, 96)
student_2 = Student('Vishaka', 10, 92)

# print(student_1.__percentage) # Error
# print(student_1.percentage)  # Error
print(student_1.get_percentage())


# Inheritence :-  Allow one class (child) to reuse the prop & methods of another class (parent).

# Parent Class - Baap
class Student:   # Student Class 
    def __init__(self, name, grade, percentage):  # Method
        self.name = name  # Attribute
        self.grade = grade  # Attribute
        self.percentage = percentage  # Attribute
    
    def student_details(self): # Method 
        print(f'{self.name} is in class {self.grade} with {self.percentage}%')  
# Object - instance of a class
student_1 = Student('Yahya', 11, 96)
student_2 = Student('Vishaka', 10, 92)

# Child Class - Beta
class GraduateStudent(Student):
    def __init__(self, name, grade, percentage, stream): # Parameters from parent class and new parameter in new child class.
        super().__init__(name, grade, percentage) # Call Parent
        self.stream = stream