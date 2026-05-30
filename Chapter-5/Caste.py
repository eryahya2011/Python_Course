# Caste In Python

a = 1 # ---> Integer
print(type(a))

b = "1" # ---> String
print(type(b))

print(a+b) # This will give an error because we cannot add an Integer and a String 

c = int(b) # Casting String to Integer
print(type(c))

print(a+int(b))  # ---> Now the String will be converted to Integer and then it will be added.

name = "Yahya"
newname = int(name) # ---> Error.  Only Number Representing Strings could converted.

num = 44
newnum = str(num) # ---> Casting Integer to String
print(type(newnum))

