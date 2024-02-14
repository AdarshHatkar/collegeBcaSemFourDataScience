#trying to understand data of netflix_data.csv file 

import pandas as pd

#Reading from a CSV file using pandas

netflix_data = pd.read_csv('practice/netflixData/netflix_titles.csv')


# print("Data frame from csv :\n",netflix_data)

# we know  there are 12 columns in the csv file and 8807 rows

# print(netflix_data.head()) #prints first 5 rows of the data

# netflix_data.info() #prints the information about the data

# print(netflix_data.describe()) #prints the statistical information about the data

# this data is from 1925 to 2021

print(netflix_data.columns.to_list()) #prints the columns of the data

# print(netflix_data['type'].unique()) # type column has 2 unique values ['TV Show' 'Movie']

# print(netflix_data['rating'].unique()) # rating column has 14 unique values and also has some invalid values like nan 74 min etc

# this data contain rating according to western countries

# TODO: create new column for indian rating 
# https://rating-system.fandom.com/wiki/Central_Board_of_Film_Certification  reference for indian rating system

# print(netflix_data['rating'].value_counts()) #prints the count of each unique value in the rating column

#  removing the invalid values from the rating column 

# print(netflix_data['rating'].isna().value_counts()) #prints the count of nan values in the rating column

# for row  in :
#     print( row)

netflix_data = netflix_data.dropna(subset=['rating']) #drops the rows with nan values in the rating column

# drop data who have rating contain min in it

# CAUTION: This is wrong move because we can fix this columns 
# we got mins in rating column because duration is the next column 
# netflix_data = netflix_data[~netflix_data['rating'].str.contains('min')]

# print(netflix_data['rating'].value_counts())

# netflix_data.info() #prints the information about the data

# print(netflix_data['description'].unique().__len__()) #prints the count of unique values in the show_id column

# here we find that there is lot of invalid data in our source  

for index, row in netflix_data.iterrows():
    if 'min' in row['rating']:
        duration = row['rating']
        netflix_data.loc[index, 'rating'] = 'Unknown'
        netflix_data.loc[index, 'duration'] = 'duration'
        # print(row)
        # print('------------------------')

    
# print(netflix_data['rating'].value_counts())