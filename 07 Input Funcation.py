# Input funcation in python
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable.

# basic input program
x = input()  # user will give some input which then store in variable 'x'
print(x)  # then we'll call print that will gives the value of 'x' as output

# Note: input funcation take input as a string form user, we can use typecasting as our own conveniance.
a = input("Enter your first name: ")
b = input("Enter your last name: ")
c = input("Enter your age: ")
print("Hello, My name is", a, b, ", I am", c, "years old.")
# In this 'c' is not taking your age as integer but as string, if your enter your age in alphabeticle form (e.g. 16 - Sixteen) it won't give error as well, but if you want it as interger then you need to do typecasting.

# Typecasting for input funcation
p = int(input("Enter first number: "))# this will take intput as interger only
q = int(input("Enter second number: "))# outherwise it will give error
print("The addition of", p, "and", q, "is", p + q)
# You can also typecast in the print statement, as it shows in the following statement
print("This will concatenate the value of p and q as it will converted into string:",str(p) + str(q))