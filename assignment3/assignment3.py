# Author: Rick Martin
import pandas as pd

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
print (more_employees)

#========= TASK 3 ===========

