# Author: Rick Martin

import csv
import os
import custom_module
from datetime import datetime

# read_employees
# Open csvFile, assume first line is fields followed by a line for each employee
# Store the employee information in a dictionary and return the dictionary
# References global FILEPATH
def read_employees():
    print ("Reading in employees with csv.reader!")
    listOfRows = []
    firstRow = False
    try: 
        with open(FILEPATH, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if (not firstRow):
                    # Add to dictionary with field name of "fields"
                    employees['fields'] = row
                    firstRow = True
                else:
                    listOfRows.append(row)
            employees['rows'] = listOfRows 
        return employees
    except Exception as e:
        # Handle the exception
        print(f"An error occurred: {e}")



# Assume first row of dictIn has field names in a list with name of "fields"
# Return the index in that list of fieldName
# References global variable (dictionary) employees
def column_index (fieldName):
    return (employees["fields"].index(fieldName))

# References global variable (dictionary) employees
def first_name (rowNumber):
    nameCol = column_index ('first_name')
    empRows = employees['rows']
    foundName = empRows[rowNumber][nameCol]
    return foundName

# References global variable (dictionary) employees
def employee_find (employee_id):
    employee_id_column  = column_index ('employee_id')
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# References global variable (dictionary) employees
def employee_find_2(employee_id):
   employee_id_column  = column_index ('employee_id')
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Sort the Rows by last_name Using a Lambda
# This will sort the rows list in employees
# References global variable (dictionary) employees
def sort_by_last_name ():
    rowsToSort = employees["rows"]
    rowsToSort.sort (key=lambda item: item[2])
    return rowsToSort

# return a dictionary with single entry, the empRow with the fields as keys
# References global variable (dictionary) employees
def employee_dict (empRow):
    retDict = {}
    # print ("Employee row:", empRow)
    index = 0
    for item in empRow:
        # print (item)
        # print (employees["fields"][index])
        # Skip the employee id
        if (employees["fields"][index] != "employee_id"):
            retDict.update({employees["fields"][index]: item})
        index += 1
    
    return retDict

# Return a new dictionary. Key for each entry is the employee id. 
# The value of each entry is itself a dictionary with the other properties of the employee
# References global variable (dictionary) employees
def all_employees_dict ():
    empRows = employees["rows"]
    rowNbr = 0
    retDict = {}
    for item in empRows:
        # Assume employee ID is first (0) Should have function to find that 
        employeeID =item[0]
        empSingleDict = employee_dict (empRows[rowNbr])
        retDict[employeeID] = empSingleDict
        rowNbr += 1
    return retDict

# Return value of the environment variable THISVALUE
def get_this_value():
    return os.environ['THISVALUE']

def set_that_secret (secretIn):
    custom_module.set_secret(secretIn)

# Read in two minutes files into two dictionaries
# Return those dictionaries
# Each Dictionary will have the first entry as "fields", the second entry as "rows"
# The rows will be tuples
def read_minutes():
    # MINUTES_1 = " ..\\csv\\minutes1.csv"
    MINUTES_1 = "C:\\Users\\rick-\\Documents\\CTD\\python\\python_homework\\csv\\minutes1.csv"
    # MINUTES_2 =  "../csv/minutes2.csv"
    MINUTES_2 = "C:\\Users\\rick-\\Documents\\CTD\\python\\python_homework\\csv\\minutes2.csv"

    minutes1Dict = getMinutes(MINUTES_1)
    minutes2Dict = getMinutes(MINUTES_2)

    return minutes1Dict, minutes2Dict


def getMinutes(fileIn):
    retDict = {}
    listOfRows = []
    firstRow = False

    # Open the file for reading
    with open(fileIn, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if (not firstRow):
                retDict['fields'] = row
                firstRow = True
            else:
                rowTuple = tuple (row)
                listOfRows.append (rowTuple)
    retDict['rows'] = listOfRows   
    return retDict

# References global variables minutes1 and minutes2
# Convert the two lists into sets. Return the union of the two sets
def create_minutes_set():
    setMinutes1 = set (minutes1["rows"])
    setMinutes2 = set (minutes2["rows"])
    finalSet = setMinutes1.union(setMinutes2)
    return finalSet

# References global minutes_set
# Convert minutes_set to a list
# Convert the string that is a date into a string. Put the name of recorder and date object into a tuple
# return the tuple
def create_minutes_list():
    listMinutes = list (minutes_set)
    newList = []
    #for item in listMinutes:
    #    newDate = datetime.strptime(item[1], "%B %d, %Y")
    #    print ("New date: ", newDate)
    #    newList.append ([item[0], newDate])
    return tuple(map (lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),listMinutes))

# References globals minustes_set and minutes1
# Convert date object in minuts_set to a string. Sort based on date. 
# Write the fields as first line in minutes.csv followed by each line in sorted list
# Return the sorted list
def write_sorted_list():
    OUTFILENAME = ".\\minutes.csv"
    retList = []

    # print ("Minutes list: ", minutes_list)
    sortedList = sorted(minutes_list, key=lambda x: x[1])

    with open(OUTFILENAME, 'w', newline='') as csvfile:
        headerNames = minutes1["fields"]
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow (headerNames)
        retList = list (map (lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),sortedList)) 
        csvwriter.writerows(retList)
        print ("Sorted minutes written to:", OUTFILENAME)

    return retList

FILEPATH = "C:\\Users\\rick-\\Documents\\CTD\\python\\python_homework\\csv\\employees.csv"
employees = {}
employees = read_employees ()
print ("Employees:", employees)

employee_id_column = column_index("first_name")
# print ("First name from second row: ", first_name(2))

# print (employee_find (12))
# print (employee_find_2 (12))
# rowsSorted = sort_by_last_name ()
# print ("After sort:", employees)
# rowDict = employee_dict (employees["rows"][0])
# print ("Single dictionary: ", rowDict)
# dict_result = all_employees_dict()
# print ("New employee dict:",dict_result)

# print (get_this_value())
# set_that_secret ("foo")
# print (custom_module.secret)

# print (get_this_value())

minutes1, minutes2 = read_minutes()

#print ("Minutes 1:", minutes1, "\n")
#print ("Minutes 2:", minutes2, "\n")

minutes_set = create_minutes_set()
#print ("Set of minutes: ", minutes_set)

minutes_list = create_minutes_list()
#print ("Minute list: ", minutes_list)

sortedList = write_sorted_list()
# print ("Sorted List: ", sortedList)
