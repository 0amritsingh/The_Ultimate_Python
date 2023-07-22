# Sets in Python:

# Sets are unordered collection of data items. They store multiple items in a single varible. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, means you can't change items of the set once created. Sets do not contain duplicate items.
# Note: Order of items is not in your hand it can be in any order, you can see this by runing the code multiple times.

s = {"Amrit", 2, 3.4, False, 2}
print(s)

# To access items from the set by for loop:

for i in s:
    print(i)
    
# Special Note
# if you make a empty set and print it's type you'll see its a dict.
# So, don't confuse in this, WE WILL LEARN MORE ON DICTIONARY.

a = {}
print(type(a))

b = set() # you can do this to see type set
print(type(b))
