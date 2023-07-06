# Strings in Python
# As we already studied about strings that:

# A string is define either in double cotes ("") or in single cotes ('')
# first way of defining
a = "This is"
print(a)
# second way of defining
print("a String")

# We can't write double cotes in double cotes and visa-versa
# print("This will throw an "ERROR"")
# print('This will throw an 'ERROR'')

# We can use escape sequance instead \' \"
print("This will throw an \"ERROR\"")
print('This will throw an \'ERROR\'') 

# We can add a new line by using \n escape sequance
print("this is a new line \nEscape Sequence")

# We can also create multiline string by using triple double cotes (""") and triple single cotes (''')

b="""
Hey,
I'm Amrit Singh 
of Class 11th 'A' 
in Gurukul Academy
at Jhankat
"""
print(b)

# Indexing of a String

# it means printing/taking a single character from a particular string, remember every indexing starts form 0 of any string.
c="name" # as in this n-0, a-1, m-2, e-3
print(c[0])
print(c[1])
print(c[2])
print(c[3])

# But what if we have to do indexing of a paragraph
# in this case we use For Loops

d="""
Now,
This for loop will
index all the character
of this pharagraph including 
all the spaces and new lines.
"""
for character in d:
    print(character)

# we will learn more on loops