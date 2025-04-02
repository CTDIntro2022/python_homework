# Author: Rick Martin
import pandas as pd
import numpy as np

#Use a dictionary containing the following data:
#  Name: ['Alice', 'Bob', 'Charlie']
#  Age: [25, 30, 35]
#  City: ['New York', 'Los Angeles', 'Chicago']
dict = { "Name": ['Alice', 'Bob', 'Charlie'],
        "Age": [25, 30, 35],
        "City": ['New York', 'Los Angeles', 'Chicago'] }
task1_data_frame = pd.DataFrame(dict)

task1_with_salary = task1_data_frame.copy()

# Add a new column
task1_with_salary = task1_data_frame.copy()
salaries = [70000, 80000, 90000]
task1_with_salary['Salary'] = salaries
task1_older = task1_with_salary.copy()

# Increment age
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

# Write to csv file
EMPCSV = "employees.csv"
task1_older.to_csv(EMPCSV, index=False)


#========= TASK 2 ===========
# Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
# Print it and run the tests to verify the contents.
task2_employees = pd.read_csv(EMPCSV)
# print(task2_employees)

# Load JSON file into a new DataFrame and assign it to the variable json_employees.
EMPJSON = "additional_employees.json"
json_employees = pd.read_json(EMPJSON)
# print (json_employees)

# Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees.
# Print the combined Dataframe and run the tests.
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
# print (more_employees)

#========= TASK 3 ===========
# Assign the first three rows of the more_employees DataFrame to the variable first_three
first_three = more_employees.head(3)

# Assign the last two rows of the more_employees DataFrame to the variable last_two
last_two = more_employees.tail(2)

# Assign the shape of the more_employees DataFrame to the variable employee_shape
employee_shape = more_employees.shape

# Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts.
# print (more_employees.info())

#========= TASK 4 ===========
# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
DIRTYDATA = "dirty_data.csv"
dirty_data = pd.read_csv(DIRTYDATA)
print ("Dirty data: \n", dirty_data)

# Remove any duplicate rows from the DataFrame
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()
print ("Dropped Dupes:\n", clean_data)

# Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print ("Age to numberic:\n", clean_data)

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print ("Salary to numberic:\n", clean_data)

# Fill missing numeric values (use fillna).  Fill Age with the mean and Salary with the median
ageMean = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(ageMean) 

salaryMedian = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(salaryMedian)

# print ("After replace na for salary:\n", clean_data)

# Convert Hire Date to datetime
clean_data ['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed')
print ("After date time conversion:\n", clean_data)

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Department'] = clean_data['Department'].str.upper()
clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Name'] = clean_data['Name'].str.strip()

print ("After Department and name to Upper and white space:\n", clean_data)