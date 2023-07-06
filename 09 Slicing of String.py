# Sclicing of String in python:

# Length of an String:
# If you want to know the length -number of characters- of a particular string you can use len() funcation

x = "Technology"
print("The word \"",x,"\" has", len(x), "characters in it.")

# String as an Array:
# String is a sequence of characters called an array. And we can take every characters of this array. WE WILL LEARN MORE ON 'ARRAY'.

# Sclicing of String in python:

# We can take characters of a string form a particular point to a particular point, it is writen in ratio - stringname(X:Y-1). -1 is form the pyhton like if we want 5 wards we will write 6 to get 5 as in background 6-1=5.
print(x[0:10])
# This is called sclicing of a string. As we slice a pizza form one point to another to take a part of it.
# It is also taking a part from a string, and to tell the computer that what is the intial point and the last point.

print(x[0:4])
# As we take 4 because it will changed into 4-1 i.e 3.
# 0 to 3 like 0~T, 1~e, 2~c, 3~h

# If we write nothing in the X (intial position) then pyhton take it as zero.
print(x[:6])
# And if we write nothing in the Y (Last position) then pyhton take it as the number of the last character of the particular string.
print(x[6:])
# We'll have the whole string as if we write only : (ratio symbole) in the square brackets, leaving X and Y empty.
print(x[:])

# Another Example on the same word
print(x[4:6])

# Negitive Sclicing of a String:

print(x[-6:-4])
# negitive sclicing means taking negitive numbers to obtain a desired output.
# In the above code -6 means the lenght of the varibale x i.e 10, 10-6=4 and -4 means the lenght of the varibale x i.e 10, 10-4=6
# it means [-6:-4] and [4:6] are similar.
# Python iterprits the negitive sclicing as the following code:
print(x[len(x)-6:len(x)-4])

# Another Example:
print(x[-10:])
