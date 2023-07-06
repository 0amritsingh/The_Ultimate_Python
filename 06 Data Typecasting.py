# Typecasting in Python
# the conversion of one type of datatype into another type of datatype is called typeconversion or typecasting in python

# These are of two types:
# 1. Explicit Conversion (Which the user does)----------------------------------

a = 1
b = 2

print(a + b)

# In this print statement we typecast the both integers in string
print(str(a) + str(b))
# first value of 'a' converted into a string(1 to "1"), then value of 'b' converted and then both strings has been added.

# A common mistake:
print(str(a + b))
# We think that the output of this print statement is 13 but no, because
# In this print statement firts the value of 'a' and 'b' added and it converted into string thats why the the output is 3

# Another example (float)
print(float(a) + float(b))

# 2. Implicit Conversion (which the python does)----------------------------------

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.