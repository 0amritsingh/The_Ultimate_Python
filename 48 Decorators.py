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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Decorators :If we need to run a function before and after a function then we use decorators or at the rate keyword in python.

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

# def at_the_rate(fx):
#   def decorator(*args, **kwargs):
#     before_fun()
#     main_fn(*args, **kwargs)
#     after_fun()
#   return decorator

# See this with an example:
def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
hello()
add(1, 2)
