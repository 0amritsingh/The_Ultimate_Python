# Docstring in python

# Docstrings are the strings litreals that appears right after the definition of a function, methode, class or module

def cube(num):
    """This funcation returns the cube of the given number""" 
    # This is a docstring, it should be written just after the defining of the function as it is now.
    print(num**3)
    
cube(5)
print(cube.__doc__) # you can print docstring by __doc__

# About PEP 8
# PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# The Zen of Python (Easter Egg in Python)
print("\n")
# So, this is basicaly a module to be import, honestly its a poem by Tim Peters which appear to be so relatable to a programmer. You can see by importing this 
import this # litrely "this" :D
