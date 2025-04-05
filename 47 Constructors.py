# Constructors in Python (OOPs):

# In previous lesson we saw that we can create classes and objects.
# We also created multiple objects and intialize each object indivdualy as per the class, but what if we pass class methods as the arguement in the object to make it easer to understand and recogonise.

# Notes: A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created. A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax of Python Constructor
#   def __init__(self):
#   	# initializations

# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.

class jober:
    def __init__(self, n, j):
        self.name = n
        self.job = j

    def details(self):
        print(f"I'm {self.name} and I'm a/an {self.job}")

a = jober('Amrit', 'AI dev')
b = jober('Anmol', 'Australian Immigrant')

a.details()
b.details()

# So, this was Parameterized Constructor.

# There are two types of constructors in python:

# 1. Parameterized Constructor: When the constructor accepts arguments along with self, it is known as parameterized constructor. These arguments can be used inside the class to assign the values to the data members. Example above.
# 2. Default Constructor: When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor. Example below

class animal:
    def __init__(self):
        print('This is an Default Constructor')

obj = animal()
    