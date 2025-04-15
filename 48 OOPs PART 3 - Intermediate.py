# Part 2: OOPs

# [6] del keyword - delete any object or its attribute in class
'''
class student: # created class
    def __init__(self, name):# constructor
        self.name = name # object attribute

s = student('amrit') # created object 

# performed tasks
print(s.name) # this will print the name
del s # del keyword deleted the object s
print(s.name) # so this will throw an error
'''

# [7] Private(like) attributes and methods - These are some class object and mehtods that can't be asscessable from the outside of the class but can be access within the class - To make any class object or method private just add two underscores "__" initaily making them
'''
class person: # created class

    def __init__(self, name): # constructor
        self.__name = name # class attribute (private)
    
    @staticmethod # decorator for static method
    def __hello(): # method (private)
        return 'Hello!'
    
    # you can't use these private class or methods attributes outside the class but you can use them within the class as in the following method, and of course you can use this method outside the class. But you can't use those private object and method directly.
    
    def welcome_person(self): 
        return f'{self.__hello()} {self.__name}. You are welcomed here.' 
    
p = person('amrit'.capitalize()) # create object

# performed tasks: 
print(p.__name) # this will throw error - you can't use private class attributes outside the class
print(p.__hello()) # this will throw error - you can't use private method attribute outside the class
print(p.welcome_person()) # this will exicute - we use the private class and method within this method but the method itself is not a private method.
'''

# [8] INHERITANCE - when one class(child/derived) derives the properties and mehtods of another class (parent/base) - this is of three types: single(1 parent to 1 child), mulit level(1 parent to many child), multiple(many parent to 1 or many child)

# Example 1: single
'''
class base:
    var1 = 'This varible is from base class'
class derived(base): # inheritance of all the class attibutes and methods of 'base' class to the 'derived' class
    var2 = 'This varible is from derived class'
x = derived()
print(x.var2) 
print(x.var1) # and now we can use the class attribues of base class directly form derived class
'''

# Example 2: multi level
'''
# one base class is inherited by two derived classes:
class base:
    var1 = 'This is from base class : A'
class derived1(base):
    var2 = 'This is from derived 1 class : B'
class derived2(base):
    var3 = 'This is from derived 2 class : C'

# Created objects
x = derived1
y = derived2

# performed tasks
print(x.var1)
print(x.var2)
print(y.var1)
print(y.var3)
'''

# Example 3: Mulitple
'''
# Mulitple classes inherited by one class
class C1:
    var1 = 'This is from C1 : A'
class C2:
    var2 = 'This is from C2 : B'
class C3:
    var3 = 'This is from C3 : C'
class C4(C1, C2, C3):
    var4 = 'This is from C4 : D'

# Created object
x = C4

# performed tasks
print(x.var1)
print(x.var2)
print(x.var3)
print(x.var4)
'''

# [9] super() method - this is use to access the method from parent class (mainly init constructor)
'''
class person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def details(self):
        print(f'Name: {self.name}\nAge: {self.age}\nSex: {self.sex}')
    
class change(person):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex) # we use super to change/manupulate the class attribute of person(base) class in the change(derived) class.

    def change_sex(self):
        newsex = input('Set you sex by typing:\nfor male - M\nfor female - F\nfor other - O\n> ')
        self.sex = newsex

a = change('amrit', 18, 'F')
a.details()
a.change_sex()
a.details()
'''
