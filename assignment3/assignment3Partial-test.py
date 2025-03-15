import assignment3 as a3
import numpy as np
import pandas as pd
import os


test1_df = pd.DataFrame({   'Name': ['Alice', 'Bob', 'Charlie'], 
                            'Age': [25, 30, 35], 
                            'City': ['New York', 'Los Angeles', 'Chicago']})

# Task 1
def test_data_frame_from_dictionary():
    assert test1_df.equals(a3.task1_data_frame)

def test_added_column():
    assert a3.task1_with_salary['Salary'].equals(pd.Series([70000, 80000, 90000]))

def test_increment_column():
    assert a3.task1_older["Age"].equals(pd.Series([26, 31, 36]))

def test_write_csv():
    assert os.access("./employees.csv", os.F_OK) == True
    # make sure there is no index
    assert pd.read_csv('employees.csv').shape == (3, 4)

# Task 2
def test_read_data_frame_from_csv():
    assert a3.task1_older.equals(a3.task2_employees)

test2_json_df = pd.DataFrame({ 'Name': ['Eve', 'Frank'],
                                'Age': [28, 40],
                                'City': ['Miami', 'Seattle'],
                                'Salary': [60000, 95000]})

def test_read_data_frame_from_json():
    assert os.access("./additional_employees.json", os.F_OK) == True
    assert a3.json_employees.equals(test2_json_df)

def test_concat_json_employees():
    assert a3.more_employees.equals(pd.concat([a3.task2_employees, a3.json_employees], ignore_index=True))
    assert a3.more_employees.shape == (5, 4)