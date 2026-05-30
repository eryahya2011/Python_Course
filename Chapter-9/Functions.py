# Functions in Python

# Create Function
def greetings():
    print("Hello, welcome to the world of Python programming!")

# Call Funtion (Use FUnction)
greetings()

# Create a Function to add two numbers:

def add2numbers(a,b):
    result = a + b
    print("The sum of the number is ", result)

# Call the function 

add2numbers(5,3)   # Argument

add2numbers(a=10, b=100)

add2numbers(b=50, a=20)

# Function to conveert Celsius to Fahrenheit:

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Call the function and store the result in a variable

temp = celsius_to_fahrenheit(25)
print(temp)

# Function to convert Celsius to Fahrenheit:

def celsius_to_fahrenhiet(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

celsius_to_fahrenheit(50)    