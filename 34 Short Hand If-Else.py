# Short hand if else:

# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short.

# Genral syntax:
# result = value_if_true if condition else value_if_false

# old method syntax:
# if condition:
#     result = value_if_true
# else:
#     result = value_if_false

# Here's example for better understanding:
n = int(input("Enter an Integer: "))

# Old method:
if (n < 0):
    result = f'{n} is a Negitive Integer'
    print(result)
elif (n > 0):
    result = f'{n} is a Positive Integer'
    print(result)
else:
    result = f'{n} is a Zero'
    print(result)

# Short cut method:
result = print(f'{n} is a Negitive Integer') if n<0 else print(f'{n} is a Positive Integer') if n>0 else print(f'{n} is a Zero')

# Conclusion:
# The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
# However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.
