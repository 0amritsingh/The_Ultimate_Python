# Introduction to Object-Oriented Programming (OOP) in Python:

# There are two main ways to write programs:

# Procedural Programming – the way we’ve mostly been coding so far, step-by-step instructions.

# Object-Oriented Programming (OOP) – a newer way where we use “objects” to model real things.

# In OOP, we work with two main things:

# 🧱 Class: It’s like a blueprint or a plan. For example, a “Person” class can define things like name, age, and actions like speak() or walk().

# 👤 Object: This is a real thing made using the class. For example, if the class is “Person,” then Amrit or Rahul would be actual objects with their own names and ages.

# Key Features of OOP:

# Encapsulation: Keeps the data safe. You can't directly touch an object's data; you must use its methods. It's like locking data in a box and only opening it with the right key.

# Inheritance: You can create a new class based on an existing one. For example, you can make a “Student” class from the “Person” class and add extra features.

# Polymorphism: One function can work in different ways depending on the object. For example, the same function name can be used for different classes.

# In short: OOP helps us organize code better, reuse it, and model real-world things more easily using classes and objects.

#____________________________________________________________________#____________________________________________________________________

# Classes and Objects:

# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Creating Class:
class youth:
    name = 'Amrit'
    age = 17
    def info(self):
        print(f"My name is {self.name}, I'm {self.age} years old.")

# Creating Object:
obj = youth()
# Printing values from class using object
print(obj.name)
print(obj.age)

# NOTE: now these values are default values that are given in the class (as a blueprint or as a template you can say).

# Self parameter:
obj.info()
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

# Let's create some more object for better understanding:

obj1 = youth()
obj2 = youth()
obj3 = youth()

obj1.name = 'Anmol'
obj1.age = 18

obj2.name = 'Manav'
obj2.age = 17

obj3.name = 'Vivek'
obj3.age = 17

print('\n')
print(obj1.name)
print(obj1.age)
obj1.info()

print('\n')
print(obj2.name)
print(obj2.age)
obj2.info()

print('\n')
print(obj3.name)
print(obj3.age)
obj3.info()

# NOTE: *Imortant Points* - The four pillars of OOPs in python are:

# Encapsulation: Bundling data (attributes) and methods that operate on the data into a single unit (class). It restricts direct access to some of an object's components and prevents the accidental modification of data.

# Inheritance: Creating a new class (subclass or derived class) from an existing class (superclass or base class). It promotes code reuse and establishes a relationship between classes.

# Polymorphism: The ability of different classes to respond to the same method call in their own specific way. It allows objects of different types to be treated as objects of a common type.

# Abstraction: Hiding complex implementation details and exposing only essential information to the user. Abstract classes and methods define a common interface for different subclasses, without specifying how they should be implemented.
    