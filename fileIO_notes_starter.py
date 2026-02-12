"""
Name:
Demonstrates reading, writing, and appending to a text file
"""

# 1 - Creating and writing to a file
print("Creating a text file object with the open() function \
and writing to it with the .write() method...")

# open() built-in function - 1st argument is file name to open, 2nd is the file access mode

# .write() method writes strings to a file


# 2 - Reading from a file
print("\nReading from the newly created file...")

# .read() method reads characters from a file and returns as a string


# .readline() method - Reading a line from a file
print("\nReading one line at a time...")


# Looping through a file object directly
print("\nLooping through the file, line by line...")


# .readlines() method - Reading a file into a list
print("\nReading the entire file into a list...")


# 3 - Write a file's contents using the .writelines() method
print("\nWriting a text file using the writelines() method...")


# 4 - Reading the new file using a 'with statement'
#       Eliminates the need to keep track of opened files and remember to close them.
#       File is automatically closed when the indented block ends.
print("\nReading and printing the new file using a 'with statement'...")


# 5 - Append access mode
#       Appends ("a") new data to an existing .txt file
#       without overwriting the old data, like in "w" mode.

# Append 3 more items to the grocery list and display the full list.
print ("Adding 3 more items...\n")

