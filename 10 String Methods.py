# String Methods in Python:

# Concept of Immutability:
# In Python, an immutability of a string means that once a string is created, its cannot be changed. It's like a locked box where the letters inside cannot be added, removed, or modified.
# The use of string methods modifies the string but by makeing  a copy of that string and then modify it. Its completely a new string.
# for an instant-
# a = "good"
# b = a.upper()
# print(a)
# print(b)
# 'b' is completely a new string which is modified copy of 'a'.

# ------------------------------------------------------------------

# String Methods in Python:
# Python provides a set of built-in methods that we can use to alter and modify the strings.

# upper() :
# The upper() method converts a string to upper case.
a = "this text is in the upper case"
print(a.upper())


# lower() :
# The lower() method converts a string to lower case.
b = "This Text is in The LOWER Case"
print(b.lower())


# strip() :
# the strip() removes all trailing characters from both LEFT & RIGHT.
c = ">>>HELLO<<<"
print(c.strip("><"))
# NOTE: if you don't give any attribute, then it will remove whitespace only.
c2 = "     Extra spaces removed     "
print(c2.strip())


# lstrip() :
# the lstrip() removes all trailing characters only from LEFT hence the name Lstrip (where l stand for LEFT).
d="!!!Hey!!!"
print(d.lstrip("!"))
# NOTE: if you don't give any attribute, then it will remove whitespace only.
d2 = "    hello    "
print(d2.lstrip())


# rstrip() :
# the rstrip() removes all trailing characters only from RIGHT hence the name Rstrip (where r stand for RIGHT).
d="!!!Hey!!!"
print(d.rstrip("!"))
# NOTE: if you don't give any attribute, then it will remove whitespace only.
d2 = "    hello    "
print(d2.rstrip())


# replace() :
# The replace() method replaces 'all occurences' of a string with another string.
e="He is Ramesh. Ramesh plays football."
print(e.replace("Ramesh", "Suresh"))


# split() :
# The split() method splits the given string at the specified instance and returns the separated strings as list items. WE WILL LOOK INTO 'LIST' IN DEPTH LATER
f="Ramesh,Suresh,Kamlesh,Mahesh,Jayesh"
print("List of the students are:", f.split(",")) # Splits the string at the commas.
# There is method called join which does opposite of split.


# join(): 
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
l1 = ["this", "is", "list"]
l2 = ("this", "is" , "tuple")
l3 = {"1": "this", "2": "is" ,"3": "dict" }
sep = " " # this is a seperator to saperate the items of the iterable, in this case it is a white space it can be any other character like alphabets or numbers.
print(sep.join(l1))
print(sep.join(l2))
print(sep.join(l3)) # Note: When using a dictionary as an iterable, the returned values are the keys, not the values. AND THE KEYS MUST BE A sting NOT AN int. 


# capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
g="first Letter of the Sentence is Capitle and Rest are SMALL."
print(g.capitalize())


# center() :
# The center() method aligns the string to the center as per the parameters given by the user.
h="Center"
print(h.center(50))
# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
h2="Center"
print(h2.center(50, "*"))


# find() :
# The find() method searches for the 'first occurrence' of the given value and returns the index where it is present. If given value is absent from the string then return -1.
i="Find the word JOKE by using find string method"
print(i.find("JOKE"))
print(i.find("joke")) # use the upper case if it in that
# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not
i2="Find the word JOKE by using find string method"
print(i2.find("JOKER"))


# index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
j="I want this word LUCK , otherwise thow an error. Oh! man there is no LUCK"
print(j.index("LUCK"))
# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
j2="I want this word LUCK , otherwise thow an error"
# print(j2.index("FUCK")) # This will thow an error
# If you need to check occurrence of a given string from a paricular point to another point you can check by indexing in it like (str.index("string", 3, 8))
print(j.index("LUCK", 25, 73))


# swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
k="upper LOWER"
print(k.swapcase())


# title() :
# The title() method capitalizes each letter of the word within the string.
l="this is a heading"
print(l.title())


# partition():
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements
l = "I love you so much"
print(l.partition("you"))
# It'll convert everything before the "match", the "match" and everything after the "match"


# format():
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# The format() method returns the formatted string
# Know more: https://www.w3schools.com/python/ref_string_format.asp
txt1 = "My name is {name}, I'm {age}" # by naming
txt2 = "My name is {0}, I'm {1}" # by indexing 
txt3 = "My name is {}, I'm {}" # by leaving it blank
print(txt1.format(name = "John", age = 36))
print(txt2.format("John",36))
print(txt3.format("John",36))


# ------------------------------------------------------------------
# Now the following methods gives Boolean outputs i.e Ture or False: 
# ------------------------------------------------------------------

# endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
m="This is sentence is ending with a name"
print(m.endswith("name"))
# We can even also check for a value in-between the string by providing initial and final index positions.
m="This is sentence is ending with a name"
print(m.endswith("is", 3, 19)) # i-18 so, 19-1=18 because Y-1


# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
n="ThisIsString1" # Ture
print(n.isalnum())
n2="This Is String 1" # False
print(n2.isalnum())


# isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
o="ThisIsStringTwo" # Ture
print(o.isalpha())
o2="ThisIsString2" # False
print(o2.isalpha())


# islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
p="this is lower" # Ture
print(p.islower())
p2="This is UPPER" # False
print(p2.islower())


# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False. Like escape sequences \n, \', etc
q="this is printable" # True
print(q.isprintable())
q2="this is not printable\n" # False
print(q2.isprintable())


# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False. It can both created with 'tab' and 'spacebar'.
r="     " # True
print(r.isspace())
r2="NoSpace" # False
print(r2.isspace())


# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
s="It Is A Title" # True
print(s.istitle())
s2="not a Title" # False
print(s2.istitle())


# isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
t="UPPER" # True
print(t.isupper())
t2="lower" # False
print(t2.isupper())


# startswith() :
# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
u="Yo Yo Honey Singh"
print(u.startswith("Yo"))
# We can even also check for a value in-between the string by providing initial and final index positions.
u="Yo Yo Honey Singh"
print(u.startswith("Yo",3 , 7))
