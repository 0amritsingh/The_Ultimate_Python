# Types of ERROR in Python:

# 1. SyntaxError - Missing Parentheses:
'''
print("Hello, world"
'''
# OUTPUT: SyntaxError - Missing closing parenthesis in the print function.

# 2. IndentationError - Incorrect Indentation:
'''
if True:
print("Indentation is important!")
'''
# OUTPUT: IndentationError - Inconsistent or missing indentation within the if block.

# 3. NameError - Undefined Variable:
'''
x = 10
print(y)
'''
# OUTPUT: NameError - Trying to access an undefined variable y.

# 4. TypeError - Incompatible Data Types:
print("42" + 8)
# OUTPUT: TypeError - Attempting to concatenate a string and an integer.

# 5. IndexError - Accessing Out-of-Range Index:
my_list = [1, 2, 3]
print(my_list[3])
# OUTPUT: IndexError - Trying to access an index that is out of range for the list.

# 6. ValueError - Incorrect Conversion:
print(int("hello"))
# OUTPUT: ValueError - Trying to convert a non-numeric string to an integer.

# 7. KeyError - Accessing Nonexistent Dictionary Key:
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])
# OUTPUT: KeyError - Accessing a key that doesn't exist in the dictionary.

# 8. FileNotFoundError - Opening Nonexistent File:
with open("nonexistent.txt", "r") as file:
    content = file.read()
# OUTPUT: FileNotFoundError - Trying to open a file that doesn't exist.

# 9. ZeroDivisionError - Division by Zero:
print(10 / 0)
# OUTPUT: ZeroDivisionError - Attempting to divide by zero.

# 10. AttributeError - Calling Nonexistent Method:
my_list = [1, 2, 3]
length = my_list.length()
# OUTPUT: AttributeError - Trying to call a method that doesn't exist for the list.

#These examples should give beginners an idea of the kinds of errors they might encounter and help them understand the error messages better.
