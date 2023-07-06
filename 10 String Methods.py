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

# The strip() method removes any white spaces before and after the string.

c="                   Extra spaces removed                   "
print(c.strip())


# rstrip() :

# the rstrip() removes any trailing characters.

d="Hey!!!"
print(d.rstrip("!"))

# I does't removes intial trailing characters

d2="#Hey#"
print(d2.rstrip("#"))


# replace() :

# The replace() method replaces 'all occurences' of a string with another string.

e="He is Ramesh. Ramesh plays football."
print(e.replace("Ramesh", "Suresh"))


# split() :

# The split() method splits the given string at the specified instance and returns the separated strings as list items. WE WILL LOOK INTO 'LIST' IN DEPTH LATER

f="Ramesh,Suresh,Kamlesh,Mahesh,Jayesh"
print("List of the students are:", f.split(",")) # Splits the string at the commas.


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

# ------------------------------------------------------------------
# Now the following methods gives Boolean outputs i.e Ture or False: 
# ------------------------------------------------------------------

# endswith() :

# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

m="This is sentence is ending with a name"
print(m.endswith("name"))

# We can even also check for a value in-between the string by providing start and end index positions.

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

# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

u="Yo Yo Honey Singh"
print(u.startswith("Yo"))

# We can even also check for a value in-between the string by providing start and end index positions.

u="Yo Yo Honey Singh"
print(u.startswith("Yo",3 , 7))
