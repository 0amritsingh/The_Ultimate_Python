# Finally Block

# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end.
# The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.


# This is the one of the example of finally block:
try:
    x = int(input("Enter an integer: "))
    print(x)
    print("*other line of code*")
except:
    print("The value entered by you is not an integer. Try Again!")
finally:
    print("I will always executed")
    
    
# But Some people will say why should I use finally if I can do the same thing by writing this (line no. 25):
try:
    y = int(input("Enter an integer: "))
    print(y)
    print("*other line of code*")
except:
    print("The value entered by you is not an integer. Try Again!")
print("I will always executed")


# But using finally is very important if you are in a function. The following example shows that if you don't use finally block you can't print the that massage. And this is not only about printing something but concider if you are working with file and you have to close the file which is important and you don't use finally block. You'll end up getting frustrated tbh.
def func2():
    try:
        z = int(input("Enter an integer\nif the value is int then system will return 1\nbut if the value is str then system will return 0\n>>> "))
        print(f"you enterd {z} which is an integer.")
        return 1
    except:
        print("The value entered by you is not an integer. Try Again!")
        return 0
    print("I will always executed")
print(func2())


# This example shows that if you use finally block then you will get your desired output. Due to this nature of finally block some interviewers ask questions about it and a lot of people don't answer it.
def func1():
    try:
        z = int(input("Enter an integer\nif the value is int then system will return 1\nbut if the value is str then system will return 0\n>>> "))
        print(f"you enterd {z} which is an integer.")
        return 1
    except:
        print("The value entered by you is not an integer. Try Again!")
        return 0
    finally:
        print("I will always executed")
print(func1())


# * INTERVIEW INSIGHTS *
# Queston: What is the purpose of the finally block in exception handling?
# Answer: The finally block is used to define code that must be executed, regardless of whether an exception occurred or not. It’s often used for cleanup tasks, such as closing files or releasing resources.

# * USE CASES *
# 1. revocing the established database
# 2. file cleanup
# 3. closing file 
# e.g: 
try:
    # Open a file
    file = open("myfile.txt", "w")
    # Write some data to the file
    file.write("This is some data.")
except Exception as e:
    # Handle the exception
    print(e)
finally:
    # Close the file
    file.close()
 
