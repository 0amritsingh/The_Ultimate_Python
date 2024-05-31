# File input/output in Python

# We can work in a text file, binary file, and even in CSV file in python. We can manupulate data in these file like CURD (create, udate, read, delete) operations.
# For that following steps are given:
# 1. creating a file
# 2. opening of a file
# 3. writing/reading a file
# 4. closing a file (most important)

# Let's see an example to get better understanding of the syntax:

# We created a text file in the same workspace with a name 'textfile.txt'.
file = open("example.txt", "r")
# Opening a file by Entering the name of the file with read (r) mode. Remember if you entered incorrect name of the exiting file or the file is not created (specialy in read mode) you'll see error.

content = file.read() # storing the content of a file in a variable.
print(content) # printing the content
file.close() # closing the file

# Closing the file is most important part. Because if you don't close the file then the other lines of code shell run into the file menupulation and you might get error.

# MODE: it is just a indication to the python that what we are going to do in the file like write, read, create, write in binary, read in binary, more.

# Types of Modes:
modes = '''
1. read (r):
This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

2. read binary (rb):
Opens the file in binary and read-only mode.

3. read-write (r+ or +r):
Opens the file in both read and write mode.

4. write (w):
Opens the file in write mode. If the file already exists, all the contents will be overwritten. If the file doesn't exist, then a new file will be created.
W can also do write binary (wb).

5. write-read (w+ or +w):
Opens the file in write and read mode.

6. append (a):
This mode opens the file for appending only and creates a new file if the file does not exist.

7. append-read (a+ or +a):
Opens the file in append and read mode. If the file doesn't exist, then it will create a new file.

8. create (x):
This mode creates a file and gives an error if the file already exists.
'''
print(f"Types of modes\n{modes}")


def reading():
    # Reading a file:
    f1 = open("textfile.txt", 'r') # mode - r
    text = f1.read() # This funcion is for reading the content of the file.
    print(text) # Printing the contect.
    f1.close()

def writing():
    # Writing a file:
    f2 = open("textfile.txt", "w") # mode - w
    f2.write("hey i'm writing in this file")
    # This function is to write a single line, for multiple lines use "\n".
    # writelines() is simmilar funcation but it is use with loop like you want to add line by line. 
    f2.close()

    # NOTE: write function rewrite the entire file (it delete the content then write the new one) and if you don't want to lose the previous content you need to use 'a' means append mode.

def appending():
    # Appending a file:
    f3 = open("textfile.txt", "a") # mode - a
    f3. write("\nThis text is appended to this file")
    # This function will appended line of content without overwriting.
    f3.close()

def with_clause():
    # The 'with' clause:
    with open("textfile.txt", "r") as f4:
        print(f4.read)
    # Using this clause you don't need to close file.


# Run funtion accordingly to see how things works:
# reading()
# writing()
# appending()
# with_clause()
