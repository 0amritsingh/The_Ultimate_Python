# Part 1: OOPs

# [1] classes and objects - class is a blueprint or a template for objects to be created after that
# [2] class and instance attributes - class.attr (common for all objects) and obj.attr (valued individualy i.e self.something = something)
# [3] constructor - __init__ function
# [4] methods - the funcation we make in the class - always use self as an attribute in each method you make
# [5] static method - decorator - in which we don't need a self - but we can work with class attributes in it

class student: # Created class

    collage = 'NIT Trichy' # class attributes
    name = 'default' # if class.attr and obj.attr are of same name then the prefrence will be higher for obj.attr (class.attr < obj.attr)

    def __init__(self, name, branch): # constructor
        self.name = name # object attribute
        self.branch = branch # object attribute

    @staticmethod # decorator
    def welcome(): # static method
        print(f'Hello, wellcome to {student.collage}')

    def detail(self): # methods
        self.welcome() # we can also use student.welcome()
        print(f'Name: {self.name}, Branch: {self.branch}')

s1 = student('Amrit Singh', 'CSE + AI') # Created object

# Practices: 
s1.detail()
print(student.collage)
print(s1.collage)
print(student.name)
print(s1.name)
s1.welcome()
    