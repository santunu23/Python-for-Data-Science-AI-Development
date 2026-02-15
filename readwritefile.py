#Open file in python
# File mode in python 
# 'r'=Read mode. Opens an existing file for reading. Raises an error if the file doesn't exist.
# 'w'= Write mode. Creates a new file for writing. Overwrites the file if it already exists.
# 'a'= Append mode. Opens a file for appending data. Creates the file if it doesn't exist.

# file= open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file.txt','r')
# line1=file.seek(11)
# line2=file.readline()
# print(line1)
# print(line2)

# file= open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file.txt','r')
# file.seek(11)
# while True:
#     line=file.readline()
#     if not line:
#         break
#     print(line)

# with open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file.txt','r') as file1:
#     i=0;
#     for line in file1:
#         print("Iteration",str(i),": ",line)
#         i=i+1


#Write file using python
# with open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file1.txt','w') as file1:
#     file1.write("This is line A\n")
#     file1.write("This is line B\n")

#Write a document/file using a list.'w' will overwrite the data.
# Lines=["This is line A\n"]
# with open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file2.txt','w') as file1:
#     for line in Lines:
#         file1.write(line)

#Copying contents from one file to another.
# with open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file.txt','r') as readfile:
#     with open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file1.txt','w') as writefile:
#         for line in readfile:
#             writefile.write(line)

#We can also use appending data(a) mode when opening a file to append new data to an existing file without overwriting it content
# new_data="This is line C"
# with open('Python for Data Science, AI & Development/Python-for-Data-Science-AI-Development/file.txt','a') as file1:
#     file1.write(new_data+"\n") 


# Pandas for data loading

# csv_path='file1.csv'
# df=pd.read_csv(csv_path) #df কে আমরা ডাটাফ্রেমের শর্ট হিসেবে ধরা হয়েছে।
# df.head()

# # loading an excel file is similliar
# xlsx_path='file1.xlsx'
# df=pd.read_excel(xlsx_path)
# df.head()

# Create a Series from a list
# import pandas as pd
# data = [10, 20, 30, 40, 50]
# s = pd.Series(data)
# print(s)
# print(s[2]) #Access the element with label 2
# print(s.iloc[3]) # Access the element at position 3
# print(s[0:3]) #Access a range of element by label


# Dataframe is a two-dimensional  labeled data structure with columns of potentially different data types.

import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df=pd.DataFrame(data)
# print(df)
#Access the `Name` column
#print(df['Name'])

# Access rows using .iloc[]
# print(df.iloc[2])
# print(df.iloc[1])

# print(df[['Name','Age']]) #Select specific columns
# print(df[1:3])  # Select specific rows

# Find unique elements


import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df=pd.DataFrame(data)
# unique_dates=df['Age'].unique()
# print(unique_dates)

#Conditional Filtering
import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df=pd.DataFrame(data)
high_above_102=df[df['Age']>25]
print(high_above_102)


Slicing
df.loc[1, 'Total'] 
df.iloc[0:2, 0:3]
