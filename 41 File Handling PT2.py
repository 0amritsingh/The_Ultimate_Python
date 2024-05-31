# readline(), readlines() and writelines() funcations for File Handling:

# Meaning/Definetion of the funactions:
meaning = '''
read() : read entire content of the file

write() : write content in the funcation in one go (you can write one line or write mulitpal lines by using \\n). It rewrites the entire content if you write again in the same file.

append() : It is use to append content after some already written content. It remove the problem of rewriting.

readline() : reads only one line of the file content. We can use loops to read multiple lines

readlines() : The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop. It reads all the lines of the file and returns them as a list of strings.

writelines() : The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple. Keep in mind that this funcation does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately
'''
print(f'Meaning/Definetion of the funactions:\n{meaning}')

# See the following examples to get better understanding:

# Reading file using readline() function:
with open("textfile.txt", 'r') as f:
    line = f.readline()
    print(line) # prints the 1st line
    print(line) # prints the 2nd line
    print(line) # and so on....

# Reading muliple lines using readline() function:
with open("textfile.txt", "r") as f:
    while True:
        lines = f.readline()
        print(lines, end="")
        if not lines:
            break

# Reading muliple lines using readlines() function:
with open("textfile.txt", "r") as f:
    for i in f.readlines():
        print(i, end='')

# Writing muliple lines using writelines() function:
with open('textfile.txt', 'w') as f:
    lines = ['line 1\n', 'line 2\n', 'line 3\n']
    f.writelines(lines) # it takes and gives the list only

# Writing muliple lines by taking input from user:
with open("textfile.txt", 'w') as f:
    lines = []
    for i in range(int(input('Enter no of lines: '))):
        lines.append(input(f"Enter Line {i+1}:\n>>> ") + '\n')
    f.writelines(lines)

# Appending muliple lines by taking input from user:
with open('textfile.txt', 'a') as f:
    for i in range(int(input('Enter no of lines: '))):
        f.write(input(f"Enter line {i+1}:\n>>>  ")+'\n')
