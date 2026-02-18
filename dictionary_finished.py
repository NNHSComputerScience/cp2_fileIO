# A Python dictionary is a collection of key-value pairs. 
#   Each key is connected to a value, and you can use a key to access the value associated with it.
#   A key’s value can be a number, a string, a list, or even another dictionary.
#   In Python, a dictionary is wrapped in braces, {}, with 
#   a series of key-value pairs inside the braces, as shown in the following example:
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print("Starting dictionary:\n", dictionary)

# add a key-value pair to a dictionary
dictionary['key4'] = 'value4' 
print("\nadd a key-value pair to a dictionary:\n", dictionary) 

# access a value in a dictionary
print("\naccess a value in a dictionary:\n", dictionary['key1'])
print("\naccess a value in a dictionary using get method:\n", dictionary.get('key1'))

# update a value in a dictionary
dictionary['key1'] = 1 
print("\nupdate a value in a dictionary:\n", dictionary) 

# remove a key-value pair from a dictionary
del dictionary['key2'] 
print("\nremove a key-value pair from a dictionary:\n", dictionary) 
dictionary.pop('key3') 
print("\nremove a key-value pair from a dictionary using pop method:\n", dictionary) 

# Open the file for reading
try:
    file = "infinity_war.txt"
    reader = open(file, "r")
except FileNotFoundError:
    print(f"The file {file} was not found.")

# Dictionary to hold character name (key) and how many times they spoke (value)
characters = {}

# Read each line of the file
for line in reader.readlines():
  if ":" in line:
    # Check if the character is already in the dictionary
    colon = line.index(":")
    speaker = line[0:colon].strip()
    if speaker in characters:
        # increment the count for the character
      characters[speaker] += 1
    else:
      # create new entry in dictionary for the character
      characters[speaker] = 1

reader.close()
print("\nCharacter dictionary:\n", characters)

# Max algorithm to find the character who spoke the most in the movie and how many times they spoke
maximum = 0
maxSpeaker = "None"
for speaker in characters:
  if (characters[speaker] > maximum):
    maximum = characters[speaker]
    maxSpeaker = speaker

# Print the character who spoke the most
print(f"\n{maxSpeaker} spoke {maximum} times during Infinity War, which was more than any other character.")