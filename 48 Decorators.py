# Decorators in Python: 

# ~> *args and **kwargs: 
# In Python, *args and **kwargs are used when you want to define functions that can take a variable number of arguments.

# 1. *args (Non-keyword arguments):
# Allows a function to accept any number of positional arguments (like regular variables). Internally, it’s treated as a tuple.

# Example:
# def greet_all(*args): for name in args: print(f"Hello, {name}!")
# greet_all("Amrit", "Ravi", "Sneha")
# Output:
# Hello, Amrit!
# Hello, Ravi!
# Hello, Sneha!

# 2. **kwargs (Keyword arguments):

# Allows a function to accept any number of keyword arguments (i.e., name=value). Internally, it’s treated as a dictionary.

# Example:
# def print_info(**kwargs): for key, value in kwargs.items(): print(f"{key} = {value}")
# print_info(name="Amrit", age=17, subject="Maths")
# Output:
# name = Amrit
# age = 17
# subject = Maths

# 3. You can also combine them:

# def show_all(*args, **kwargs): print("Positional args:", args) print("Keyword args:", kwargs)
# show_all("apple", "banana", fruit="mango", count=2)
# Output:
# Positional args: ('apple', 'banana')
# Keyword args: {'fruit': 'mango', 'count': 2}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

