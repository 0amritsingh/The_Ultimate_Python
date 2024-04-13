# Raising Errors in Python

# In python, we can raise custom errors by using the "raise" keyword.
# We learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

# For example, let's say that we are working with a server and server set on fire. So, we can't work with server's data obviousely. In that case I need to raise a custom error so that I can stop the further excuetion of code.

# Another example, I've make a calculator but the user is entering his wife's name instead of doing fkn calcutlation. In that case I need to raise a custom error.

# The following code is a kewl example: 

n = int(input("Enter a number between 0 and 9\n>>> "))
if n<0 or n>9:
    raise ValueError("Your number is either greater then 9 or less then 0. Try Again!")
else:
    print(f"You entered {n}")
    
# * QUICK QUIZ *
# write the same following code but add a thing in which if user write "quit" then the program ends with a massage: *you quited the program*.
 