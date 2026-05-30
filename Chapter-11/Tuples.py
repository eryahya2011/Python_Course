# Tuples In Python

my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))


# CREATING TUPLES:

# 1. Using parentheses:
my_tuple = (1,2,3)
print(my_tuple)

# 2. Mixed:
my_tuple1 = (1, "Yahya", 3.14, True)
print(my_tuple1)

# 3. Without parentheses:
my_tuple2 = 1, 2, 3
print(my_tuple2)

# 4. Tuple Constructor:
my_tuple3 = tuple((1,5,8))
print(my_tuple3)

list = [1,2,3]
new_tuple = tuple(list)
print(new_tuple)

# 5. Single element tuple:
a = ("a")
print(type(a)) # This will be a string, not a tuple

b = ("a",)
print(type(b)) # This will be a tuple

# 6. Accessing Tuple Elements:

fruits = ("apple", "banana", "cherry")
print(fruits[0]) # Output: apple
print(fruits[-1]) # Output: cherry

# 7. Tuple Slicing: 
numbers = (10 ,20, 30, 40, 50)
print(numbers[1:4]) # Output: (20, 30, 40)
print(numbers[:3]) # Output: (10, 20, 30)


# TUPLE OPERATIONS:

# Concatenate :
number1 = (1, 2, 3)
number2 = ( 'a', 'b')
number3 = number1 + number2
print(number3) # Output: (1, 2, 3, 'a', 'b') 

# Repetition:
number4 = number2 * 2
print(number4) # Output: ('a', 'b', 'a', 'b')

number5 = number1 * 3
print(number5) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Checking a element in a tuple:  (True/False)
number6 = (1, 2, 3)
print(10 in number6) # Output: False
print(2 in number6) # Output: True


# TUPLE ITERATION:

# for loop:
fruits = ('apple', 'banana', 'cherry')
for i in fruits:
    print(i)
# while loop:
i = 0 
while i < len(fruits):
    print(fruits[i])
    i += 1
    

# TUPLE METHODS:
color = ('green', 'blue', 'red', 'blue')

# count() method:
print(color.count('blue'))

# index() method:
print(color.index('green')) 


# TUPLE FUNCTIONS:
numbers = (2, 3, 1, 4)

#len():
print(len(numbers))

# sum():
print(sum(numbers))

# min() /max():
print(min(numbers))
print(max(numbers))

# sort:
a = sorted(numbers)
numbers_sorted = tuple(a)
print(numbers_sorted)


# TUPLE PACKING AND UNPACKING:
# Packing:
a = "Yahya"
b = 15
c = "IIT Delhi"

tuple_pack = a, b, c
print(tuple_pack) # Output: ('Yahya', 15, 'IIT')

# Unpacking:
Name , Age, College = tuple_pack
print("My name is", Name) # Output: Yahya
print("My age is", Age) # Output: 15     
print("I study at", College) # Output: IIT


# TUPLE MODIFICATION:
numbers = 10, 20, 30 
numbers[0] = 100 # This will raise an error because tuples are immutable

# How to modify a tuple:
tuple_numbers = list(numbers)
print(tuple_numbers) # Output: [10, 20, 30]

tuple_numbers[0] = 100
print(tuple_numbers) # Output: [100, 20, 30]

numbers = tuple(tuple_numbers)
print(numbers) # Output: (100, 20, 30)

