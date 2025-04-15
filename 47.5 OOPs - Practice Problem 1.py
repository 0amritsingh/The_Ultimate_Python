# Practice Problem: Create student class that takes name and marks of 3 subjects as arguments in constructor. Then creat a method to print the average.

class student:
    def __init__(self, name, p, c, m):
        self.name = name 
        self.p = p
        self.c = c
        self.m = m
    
    def avg_marks(self):
        avg = (self.p + self.c + self.m) / 3
        return avg
    
    # Extra (not asked)
    def details(self):
        details = f'Physics: {self.p}\nChemistry: {self.c}\nMathamatics: {self.m}'
        return details

# Creating Object: 
s1 = student('Amrit', 1, 1, 1)

# performing tasks: 
print(s1.avg_marks())
print(s1.details())
print(f'\nName of the student: {s1.name}\nHis/Her marks in each subject:\n{s1.details()}\nAvarage of all 3 subjects: {s1.avg_marks()}')

print('\n________________\n')

# Another Approch: 
class chattra:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
    
    def avg_mrk(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
        avg = sum/len(self.marks)    
        return avg
    
c1 = chattra('Amrit', [3,3,3])
print(c1.avg_mrk())
