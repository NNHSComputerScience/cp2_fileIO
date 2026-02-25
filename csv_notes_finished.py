# Notes on file I/O with CSV files

# CSV file (.csv) - comma-separated values; 
#   common format for sending tabular data (rows & columns) between
#   programs (e.g., Excel or Google Sheets)

with open('notes.csv', 'r') as csv_file:
    data = csv_file.readlines()

# String methods for working with strings:
#   .rstrip() can remove trailing characters from strings
#   .strip() can remove leading and trailing characters from strings
#   .split() is a string method that can separate out a string into a list
#       using a default separator (a.k.a. delimiter).
#       By default, split uses spaces as the separator. 
#       You can change the separator by passing the new 
#       separator as a argument:with
#           i.e. split(",") for CSV file data
for line in data:
    # TEACHER NOTE: print line first to see the newline characters 
    stripped_line = line.strip()
    #print(line)    #print(stripped_line)
    row_list = stripped_line.split(",")
    #print(row_list)
    column_a = row_list[0].strip()
    column_b = row_list[1].strip()
    column_c = row_list[2].strip()
    print(f"|{column_a:<25}|{column_b:^25}|{column_c:>25}|")

'''
f-strings - new string formatting technique in Python 3.6+
    f'xxxxxxxxx{expression}xxxxxxxxxxx'

aligning with f-strings:
    left-align = f'xxxxxxxxx{expression:<15}xxxxxxxxxx'
    center-align = f'xxxxxxxxx{expression:^15}xxxxxxxxxx'
    right-align = f'xxxxxxxxx{expression:>15}xxxxxxxxxx'
'''

def get_data():
    """Return a list with the """
    with open("College_Data.csv", "r") as data: 
        data_list = data.readlines()
        for line in data_list:
            line = line.rstrip().split(",")
            print(f"|{line[0]:<50}|{line[1]:^25}|{line[2]:>25}|")  

#print_data()
    
# filter/analyze the data in College_Data.csv to find the schools with:
#       <50% acceptance rate 
#       <$30,000 oos tuition 
#       >75% graduation rate
# print the name of the school and data in a formatted table
def analyze_data():
    with open("College_Data.csv", "r") as file:
        data_list = file.readlines() 
        #print(f"|{"College":<50}|{"Acceptance Rate":>25}|{"Out-of-State Tuition":>25}|{"Graduation Rate":>25}|")
        for line in data_list[1:]: # skip the header row
            line = line.strip().split(",")
            school_name = line[0]
            acceptance_rate = (float(line[3])/float(line[2]) * 100)
            acceptance_rate = round(acceptance_rate, 2)
            oos_tuition = float(line[9])
            graduation_rate = float(line[-1])
            if acceptance_rate < 50 and oos_tuition < 30000 and graduation_rate > 75:
                print(f"|{school_name[:25]:<25}|{acceptance_rate:^25.2f}%|${oos_tuition:^25,.2f}|{graduation_rate:^25.2f}%|")
#analyze_data()
