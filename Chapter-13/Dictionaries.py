# Dictionary In Python

#syntax:
# my_dict = { 'key1':'value1', 'key2': 'value2', ....}



# METHODS TO CREATE DICTIONARIES :

# Method - 1 :- Create Dictionary Using Curly Braces.

cohort = {'Course': 'Python', 'Instructor': 'Yahya', 'Level': 'Beginner'}
print(cohort)


# Method - 2 :- Using Dict() Constructor.

person = dict(name = 'Yahya', age = '15', grade = 'A*' )
print(person)
print(type(person))


# Method - 3 :- Using list of Tuples.

person2 = dict([('Name', 'Yahya'), ('Age', '15'), ('City', 'Delhi')])
print(person2)



# ACCESS DICTIONARY VALUE :

student = {
    1: 'Class-X', 
    'Name': 'Yahya',
    'Percentage': '90',
    'City': 'Delhi'
}
print(student)

print(student['Name'])  # ------> The name of student will be called out. [*.*, "Yahya" Will be the Output ]



# DICTIONARIES METHODS :


student = {
    1: "Class-X",
    'Name': 'Yahya',
    'Percentage': '90',
    'City': 'Delhi'
}


# 1. Keys :-
print(student.keys())

# 2. Values :-
print(student.values())

# 3. Item :-
print(student.items())

# 4. Get :-
#print(student['name'])      # --------> Same Output
print(student.get('name'))  # --------> Same Output

#print(student['mail'])     #  --------> Shows Error.
print(student.get('mail')) #  --------> Does Not Show Error.

# 5. Add/Modify :-
student['email'] = 'yahya@example.com'  # Add

student['grade'] = 'A'   # Modify

# Remove Items :-

# Del :-
del student['grade']
print(student)

# pop
student.pop('email')
print(student)


# Loops :-
# loop throug keys :
for keys in student:
    print(keys)

# loop through values :-
for value in student:
    print(student[value])

# using .value() method :-        
for value in student.values():
    print(value)

# loop through both key-value pair:
for keys,value in student.item():
    print(keys,value)


# Nested Dictionary:

main_studnet = {
    'student1' : {'name' : 'Yahya', 'age' : '15'},
    #'student2' ; {'name' : 'John', 'age' : '14', 'grade' : 'A'}
}
#print(main_student)
print(main_studnet['student1'])
print(main_studnet['student1']['name'])



# Dictionary Comprehentions:

my_dict = {x:x*x for x in range(1,6)}
print(my_dict)