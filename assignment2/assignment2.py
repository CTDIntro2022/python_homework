import csv
import os
import custom_module

# Remove the last character of the last word in arrIn
# Handy for \ns
# Pass by reference - modifying the original array
def removeLastCharOfLastWord (arrIn):
    lastField = arrIn[len(arrIn) - 1]
    lastField = lastField[0:len(lastField) -1]
    arrIn[len(arrIn) - 1] = lastField

# read_employees
# Open csvFile, assume first line is fields followed by a line for each employee
# Store the employee information in a dictionary and return the dictionary
def read_employees ():
    csvFile = FILEPATH
    listOfRows = []
    try:
        f = open(csvFile, "r")
        firstRow = False
        for row in f:
            if (not firstRow):
                rowFields = row.split (",")
                # Remove newlinne
                removeLastCharOfLastWord(rowFields)

                # Add to dictionary with field name of "fields"
                employees['fields'] = rowFields
                firstRow = True
            else:
                rowFields = row.split (",")
                # Remove newlinne
                removeLastCharOfLastWord(rowFields)
                listOfRows.append (rowFields)
                # employees.update ({'rows':rowFields})
                employees['rows'] = rowFields
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

# Returnv value of the environment variable THISVALUE
def get_this_value():
    return os.environ['THISVALUE']

def set_that_secret (secretIn):
    custom_module.set_secret(secretIn)

FILEPATH = "C:\\Users\\rick-\\Documents\\CTD\\python\\python_homework\\csv\\employees.csv"
employees = {}
employees = read_employees ()
print ("Employees:", employees)

employee_id_column = column_index("first_name")
print ("First name from second row: ", first_name(2))

# print (employee_find (12))
# print (employee_find_2 (12))
rowsSorted = sort_by_last_name ()
# print ("After sort:", employees)
rowDict = employee_dict (employees["rows"][0])
print ("Single dictionary: ", rowDict)
dict_result = all_employees_dict()
print ("New employee dict:",dict_result)

# print (get_this_value())
set_that_secret ("foo")
print (custom_module.secret)

print (get_this_value())
