# Part 5: OOPs

# [13] Class mehtods as Alternative Constructors - A class method belongs to the class rather than to an instance of the class - One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary

# Example: consider a class named "rectange" that has two attributes: "hight" and "width". The default constructor for the class might look like this:
'''
class rectange:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width

r = rectange(89, 39)
print(r.hight, r.width)
'''
# But what if you want to create a Rectange object from a string that contains the rectange's hight and width, separated by a comma? (basicly the formate is changed to provide data) You can define a class method named "from_string" to do this:
'''
class rectange:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
    
    @classmethod # we use class method as alternative constructor
    def from_sting(cls, sting):
        return cls(int(sting.split(',')[0]), int(sting.split(',')[1]))

data = '32,34'
r = rectange.from_sting(data)
print(r.hight, r.width)
'''
# Formate/Template for using class mehtods as altenative constructor: 
# @classmethod
# def name(cls, attribute):
#     return cls(attribute)
    
# [14] Method Overriding - Soon...

# [15] __dict__ method - This will return the class attributes in the key, value pair of a dictionary
'''
class student:
    def __init__(self, name, standerd):
        self.name = name
        self.standerd = standerd
    
s = student('Amrit', 12)
print(s.__dict__)
'''