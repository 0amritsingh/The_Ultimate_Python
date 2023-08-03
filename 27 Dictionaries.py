# Dictionaries in Python
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# Defining a Dictionary:- dict = {key:value,...}
d = {"Name":"Amrit Singh",
      "Class":11,
      "Age":16,
      "Eligiblity": True
}
print(d) # Printing d

# I. Accessing single values:
print(d["Name"]) # If the key does'nt exsits then it will throw value error.
print(d.get("Name")) # If key does'nt exists it will return none instead of error.
# print(d["Name"]) # This will throw error.
print(d.get("name")) # Return none.

# II. Accessing multiple values:
print(d.values())

# III. Accessing keys:
print(d.keys())

# IV. Accessing key-value pairs:
print(d.items())

# V. Accessing keys and values with for loop:
for key, value in d.items():
    print(f"{key} : {value}")
