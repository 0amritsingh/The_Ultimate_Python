# Part 4: OOPs

# [10] Class Method - decorator - Static mehtod can't access or modify class state and generally for utility so class methods allow us to change the class attribute from object itself - A class method is  bound to the class and receives the class as an implicit first argument - Following examples for better understanding

# Example 1: this shows that how we can't change the class attribute by an object without using a class method
'''
class student:
    name = 'default' # class attribute
    def changename(self, name):
        self.name = name # object attribute

s = student() # created object
s.changename('Amrit') # we gave some arrugement to method hoping to change the default into Amrit
print(s.name) # we print this statement it shows Amrit but it didn't change that class attribute i.e. default 
print(student.name) # because when we print this statement we knew the class attribute was not changed
'''

# Example 2: some indirect ways to change the class attribute without using the class method decorator
'''
class person:
    name = 'default'
    def changname(self, name):
        person.name = name # this is a clever move but irrelevent, what if we need both class attribute as well as object attribute

p = person()
p.changname('Amrit')
print(p.name)
print(person.name)
'''
# Example 3: using class mehtod decorator to solve the problem of using or manupulating class attribute by uing object or outside the class
'''
class car:
    name = 'default'
    @classmethod # class method decorator
    def changename(cls, name): # cls means class
        cls.name = name

c = car()
c.changename('mustang') # now with this the change directly to the class attribute
print(c.name) 
print(car.name)
'''
# NOTE: We got mainly 3 types of methods/decorators those are - 1. static method (), 2. instance method (self), 3. class method (cls)

# [11] Property - we use @property decorator on any method in the class to use the method as a property that means using a method as a object attibute - this is done to avoid calculation mistakes - see example for better understanding

# Example 1: what mistakes we can face
'''
class marks:
    def __init__(self, p, c, m):
        self.p = p
        self.c = c
        self.m = m
        self.percentage = str((self.p + self.c + self.m)/3) + '%'

s = marks(56, 38, 45)
print(s.p)
print(s.percentage)

s.p = 98
print(s.p)
print(s.percentage)
# Problem we face: in above three lines we change the physics marks still the percentage of all marks is not changed
'''

# Example 2: solve the above problem using property decorator
'''
class marks:
    def __init__(self, p, c, m):
        self.p = p
        self.c = c
        self.m = m
        # self.percentage = str((self.p + self.c + self.m)/3) + '%'

    @property
    def percentage(self):
        return str((self.p + self.c + self.m)/3) + '%'

s = marks(56, 38, 45)
print(s.p)
print(s.percentage)

s.p = 98
print(s.p)
print(s.percentage)
# Problem Solved: by using property decorator we can use any method as object attribute as well as solve these types of calculatoin mistakes
'''

# [12] POLYMORPHSIM - when the same oberator is allowed to have different meaning according to the context - like '+' can be use to add two or more integers and also two or more strings so in this way '+' operator have two different roles accoring to certain context, this is called Operator Overload - see example of complex number implimention in python using OOPs

# NOTE: In this we are using Dunder functions, A dunder (double underscore) function is a special method in Python with names like __init__ or __str__, used to define behavior for built-in operations like +, -, *, /, etc.
'''
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def printcomp(self):
        print(f'{self.real}i + {self.img}j')

    # now we make a dunder function for adding out two complex numbers by using '+' operator
    def __add__(self, anothercomp):
        real = self.real + anothercomp.real
        img = self.img + anothercomp.img
        return f'{real}i + {img}j'
    
n = complex(5, 4)
n.printcomp()
m = complex(1, 1)
m.printcomp()
j =  n + m
print(j)
'''