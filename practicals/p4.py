#Creating a dataset from a dictionary, lists, and reading from a CSV file using pandas.

import os
import pandas as pd

#Creating a dataset from a dictionary
my_dict = {
    'Name': ['Adarsh', 'Shiv', 'Ram', 'Sita'],
    'Age': [23, 34, 45, 56],
    'City': ['Khamgaon', 'Hiverkhed', 'Akola', 'Mumbai']
}

df_from_dict = pd.DataFrame(my_dict)
print("Data frame from dictionary :\n",df_from_dict)

# #Creating a dataset from a list

my_columns = ['Name', 'Age', 'City']

my_list = [
    ['Adarsh', 23, 'Khamgaon'],
    ['Shiv', 34, 'Hiverkhed'],
    ['Ram', 45, 'Akola'],
    ['Sita', 56, 'Mumbai']
]

df_from_list = pd.DataFrame(my_list, columns=my_columns)

print("Data frame from list :\n",df_from_list)

names_list = ['Adarsh', 'Shiv', 'Ram', 'Sita']

ages_list = [23, 34, 45, 56]

cities_list = ['Khamgaon', 'Hiverkhed', 'Akola', 'Mumbai']

df_from_list2 = pd.DataFrame(list(zip(names_list, ages_list, cities_list)), columns=my_columns)

print("Data frame from list2 :\n",df_from_list2)

# #Reading from a CSV file using pandas

csv_file_path = 'practicals\data_file.csv'

# if os.path.exists(csv_file_path):
#     print("File exists!")
# else:
#     print("File does not exist.")

df_from_csv = pd.read_csv(csv_file_path)

print("Data frame from csv :\n",df_from_csv)
