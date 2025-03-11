import assignment2 as a2

def test_read_employees():
    employees = a2.read_employees()
    assert employees != None
    assert a2.employees != None
    assert len(a2.employees["fields"]) == 4
    assert a2.employees["fields"][1] == "first_name"
    assert len(a2.employees["rows"]) == 20

def test_column_name():
    assert a2.column_index("last_name") == 2
    assert a2.employee_id_column != None

def test_first_name():
    print ("Employees in test: ", a2.employees)
    assert a2.first_name(2) == "Lauren"

def test_employee_find():
    match = a2.employee_find(3)
    assert match[0][0] == "3"
    assert len(match[0]) == 4

def test_employee_find_2():
    match = a2.employee_find_2(4)
    assert match[0][0] == "4"
    assert len(match[0]) == 4

def test_sort_by_last_name():
    rows = a2.sort_by_last_name()
    assert len(rows) == 20
    assert rows[0][2]== "Bowman"

def test_employee_dict():
    dict_result = a2.employee_dict(a2.employees["rows"][0])
    assert dict_result["last_name"] == "Bowman"
    assert "employee_id" not in dict_result.keys()

def test_all_employees_dict():
    dict_result = a2.all_employees_dict()
    assert len(dict_result.keys()) == 20
    assert dict_result["9"]["first_name"] == "Phillip"

def test_module():
    a2.set_that_secret ("foo")
    assert a2.custom_module.secret == "foo"

def test_env():
    assert a2.get_this_value() == "ABC"