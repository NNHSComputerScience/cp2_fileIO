"""
Name: Mr. Callaghan
Demonstrates reading, writing, and appending to a text file
"""

# 1 - Creating and writing to a file
print("Creating a text file object with the open() function \
and writing to it with the .write() method...")

# open() built-in function - 1st argument is file name to open, 2nd is the file access mode
#   "w" stands for write mode; creates file if it doesn't exist,
#   overwrites the file if it does exist
text_file = open("test.txt", "w")

# "text_file" is a File object (like a Turtle/String) and 
#   we can use, or call, methods on it
# .write() method writes strings to a file
text_file.write("Line 1\n")
text_file.write("Line 2\n")
text_file.write("Line 3\n")

# best practice is to close the file when done writing
text_file.close()


# 2 - Reading from a file
print("\nReading from the newly created file...")
#   "r" is for read-only access mode
text_file = open("test.txt", "r")

# .read() method reads characters from a file and returns as a string
doc = text_file.read() # reads the entire file in as a string
print(doc)

# There is a file pointer that moves to the end of the file;
#   must reset the pointer if we want to read again (using seek method)
text_file.seek(0)
chars = text_file.read(5) # reads 5 characters in as a string
print(chars)

text_file.seek(1)
chars = text_file.read(5) 
print(chars)
# the file continues reading where the pointer left off
#   includes escape chars (such as "\n", "\t") counting for one character
chars = text_file.read(10) 
print(chars)

# .readline() method - Reading a line from a file, up to and including the new line character
print("\nReading one line at a time...")
line = text_file.readline()
print(line)
text_file.seek(0)
line = text_file.readline()
print(line, end="")
line = text_file.readline()
print(line, end="")

# Looping through a file object directly
print("\nLooping through the file, line by line...")
text_file.seek(0)
n = 1
for line in text_file:
    print(n, line, end="")
    n += 1

# .readlines() method - Reading a file into a list
print("\nReading the entire file into a list...")
text_file.seek(0)
# reads in the file with each lines as an element in list
lines = text_file.readlines() 
print(lines)
for line in lines:
    print(line)
    if "2" in line:
        print(line)

text_file.close()
# 3 - Write a file's contents using the .writelines() method
print("\nWriting a text file using the writelines() method...")
text_file = open("groceries.txt", "w")
lines = ["Bread\n", "Milk\n", "Cheese\n", "Takis\n"]
text_file.writelines(lines)
text_file.close()

# 4 - Reading the new file using a 'with statement'
#       Eliminates the need to keep track of opened files and remember to close them.
#       File is automatically closed when the indented block ends.
print("\nReading and printing the new file using a 'with statement'...")
with open("groceries.txt", "r") as tf:
    contents = tf.read()
    print(contents)
    
#tf.read()  # lost access to file; automatically closed for us

# 5 - Append access mode
#       Appends ("a") new data to an existing .txt file
#       without overwriting the old data, like in "w" mode.

# Append 3 more items to the grocery list and display the full list.
print ("Adding 3 more items...\n")

with open("groceries.txt", "a") as tf:
    for i in range(3):
        next_item = input("What else do you want to add?")
        tf.write(next_item + "\n")

