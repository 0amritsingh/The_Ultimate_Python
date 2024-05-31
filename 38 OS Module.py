# OS Module in Python

import os

def allmethods(): # Run this funcation to get all the methods of os module at once.
    print('All Methods of OS Module is here:')
    for i,j in enumerate(dir(os), start=1):
        print(f'{i} - {j}\n')
# allmethods()

# The following are the most used/famous/important for a newbie. Explore these yourself.

# 1. getcwd
os.getcwd()
# Returns the current working directory as a string.

# 2. chdir
os.chdir('/path/to/directory')
# Changes the current working directory to the specified path.

# 3. listdir
os.listdir('/path/to/directory')
# Returns a list of the names of the entries in the specified directory.

# 4. mkdir
os.mkdir('/path/to/directory')
# Creates a new directory at the specified path.

# 5. rmdir
os.rmdir('/path/to/directory')
# Removes the specified directory. The directory must be empty.

# 6. remove
os.remove('/path/to/file')
# Removes the specified file.

# 7. rename
os.rename('old_name', 'new_name')
# Renames a file or directory from old_name to new_name.

# 8. system
os.system('command')
# Executes the command (a string) in a subshell.

# 9. path.join
os.path.join('dir', 'subdir', 'file.txt')
# Joins one or more path components intelligently. Returns a single string.

# 10. path.exists
os.path.exists('/path/to/file_or_directory')
# Returns True if the specified path exists, otherwise False.

# 11. path.isfile
os.path.isfile('file.txt')
# Returns True if the specified path is an existing regular file.

# 12. path.isdir
os.path.isdir('directory')
# Returns True if the specified path is an existing directory.
    