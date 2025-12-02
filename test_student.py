from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name : Alice\n"
        "Employee ID   : E10001\n"
        "Department    : IT\n"
        "Salary        : 55000\n"
    )

    assert employee_details("Alice", "E10001", "IT", 55000) == expected_output
