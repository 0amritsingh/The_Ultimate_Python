# Lambda Funcation in Pyhton

# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda <arguments>: <expression>

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Here is an example for better understanding:

# We write this:
def double1(x):
    return x * 2
print('This is from a user defined function:',double1(4))

# With lambda:
double2 = lambda x: x * 2
print('This is from lambda funcation:',double2(4))

# lambda funcation with a print statement:
sum = lambda a,b: print(f'{a} + {b} = {a + b}')
sum(2,3)

# Most important use case of Lambda is to use it as and attribute to a user define function. Here's is an example:

# Define a user-defined function that takes another function as an argument
def apply_function(x, func):
    return func(x) # This can be any other code

# Use a lambda function as the second argument
result = apply_function(5, lambda y: y ** 2)

print(result)  # Output: 25

    