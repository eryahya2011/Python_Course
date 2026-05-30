# Conditional Statements

# 1. if statement - It only executes when the codnition is True.

a = 26 
b = 108
if b > a:
    print("b is greater than a")

age = int(input("Enter Your Age: "))
if age >= 18:
    print("Congrats! You are an adult.")    


# 2. if-else statement - It Works for both True and False conditions.

age = int((input("Enter YOur Age: ")))
if age >= 18:
    print("Congrats! You are an adult.")
else: 
    print("You are not an adult.")


temp = int(input("Enter The Temperature: "))

if temp > 25:
    print("Its a hot day.")
else:
    print("Its a cool day.")    


# 3. if-elif-else statement - It works for multiple conditions.

Score = int(input("Enter Your Score: "))
if Score >= 90:
    print("A*")
elif Score >= 80:
    print("A")
elif Score >= 60:    
    print("B")
else:
    print("C")

# 4. Nested if statement - It is an if statement inside another if statement.

# Q. +ve, -ve, zero, even and odd.

num = int(input("Enter your number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.") 
else:
    if num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")         


# 5. Conditional Expressions - It is a one line if-else statement.

age = 26
status = "Adult" if age >= 18 else "Minor" 
print(status)

