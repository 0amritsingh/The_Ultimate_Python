# Decorators in Python

# Decorators :If we need to run a function before and after a function then we use decorators or at the rate keyword in python.

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
# Boilerpate for the decorator:
'''
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Code/function to execute before the function
        print("Something before the function runs")
        
        # Call the original function
        func(*args, **kwargs)
        
        # Code/function to execute after the function
        print("Something after the function runs")
    return wrapper
'''
# Example: 
'''
def greeting(add):
    def wrapper(*args, **kwargs):
        print('Good Morning!')
        add(*args, **kwargs)
        print('Good Bye!')
    return wrapper

@greeting # This is how you use a decorator
def add(a, b):
    print(a + b)

add(1, 2)
'''

# SOME IMPORTANT DEACORATOR:

# [1] Static Method - @staticmethod - 47 OOPs PART 2 - Basic

# [2] Class Method - @classmethod - 49 OOPs PART 4 - Advance

# [3] Property (getter) - @property - 49 OOPs PART 4 - Advance

# [4] Getter and Setter:
'''
class Person:
    def __init__(self, name):
        self._name = name
    
    @property # this is a getter
    def name(self):
        return self._name
        
    @name.setter # this is a setter
    def name(self, value):
        self._name = value

# Usage
person = Person("Alice")
print(person.name)  # Output: Alice
person.name = "Bob"
print(person.name)  # Output: Bob
'''