# Sets In Python



# Sets Operations:



# Sets using curly braces:
set1 = { "1", "2", "3"}
print(set1)

# Sets Using set constructor:
set2 = set(['1', '2', '3'])
print(set2)

# Adding Elements:

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

# Removing Elements:

fruits = {"Apple", "Mango", "Banana"}
# fruits.remove("Cherry")  # This Will Show An Error.
fruits.remove("Mango")

# Discard Elements:
fruit  = {"Apple", "Mango", "Banana"}
# fruit.discard("Cherry") # This Will Not Show An Error.
fruit.discard("Mango")



# Set Methods:

# Union: Combine elements from two sets.
setA = {1, 2, 3}
setB = {3, 4, 5}
union_set = setA.union(setB)
print(union_set)

# Union alternative:
union_set2 = setA | setB
print(union_set2) 

# Intersection: Get common elements between two sets.
set3 = {1, 2, 3}
set4 = {2, 3, 4}    
intersection_set = set3.intersection(set4)
print(intersection_set)

# Intersection alternative:
intersection_set2 = set3 & set4
print(intersection_set2)    

# Difference: Get elements that are in one set but not in the other.
set5 = {1, 2, 3}
set6 = {2, 3, 4}
difference_set = set5.difference(set6)
print(difference_set)

# Difference alternative:
difference_set2 = set5 - set6
print(difference_set2)

# Symmetric Difference: Get elements that are in either set but not in both.
set7 = {1, 2, 3}
set8 = {3, 4, 5}
symmetric_difference_set = set7.symmetric_difference(set8)
print(symmetric_difference_set)

# Symmetric Difference alternative:
symmetric_difference_set2 = set7 ^ set8
print(symmetric_difference_set2)



# Set Iteration:

# For loop:-
numbers = {1, 2, 3, 4, 5}
for i in numbers:
    print(i)

# While loop:- Does not support !!



# Set Comprehension: Create a new set by applying an expression to each item in an iterable.
squares = {x**2 for x in range(1, 6)}
print(squares)