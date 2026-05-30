# Operators

# 1. Arithmetic Operators
a = 5
b = 3
print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a%b) # Modulus
print(a//b) # Floor Division
print(a**b) # Exponentiation

# 2. Comparison Operators - Output is Boolean (T/F)
x = 20
y = 10
print(x > y ) # Greater than
print(x < y ) # Less than       
print(x == y) # Equal to
print(x != y) # Not equal to

# 3. Assignment Operators
p = 5 # Assignment operator

# 4 . Logical Operators

# Rules For 'AND' operator:
# True and True = True
# True and False = False
# False and True = False

m = 10
n = 20
print(m > 5 and n > 15) # Logical AND
print(m == 10 and n == 20) 

# Rules For 'OR' operator:

# True or False = True

print(m == 10 or n == 15) # Logical OR

# 'NOT' operator:
print(not(m == 10 and n == 20)) # Logical NOT

# 5. Identity Operators - 'is' and 'is not'

# Compares mempory location not the value.
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y) # True
print(x is z) # False

print(x is not z) # True 

# 6. Membership Operators - 'in' and 'not in'

my_list = [ "apple", "orange", "mango"]
print("apple" in my_list) # True
print("apple2" in my_list) # False
print("apple2" not in my_list) # True

# 7. Bitwise Operators - AND (&), OR (|), XOR (^), NOT (~), etc.
q = 5 # 0101 in binary
r = 3 # 0011 in binary
print(q & r) # 1 in binary - 0001 
