from student  import student_registation_details
def test_student_details():

    expected_output = (
        "Student ID:323\n"
        "Student Name:Bhagya\n"
        "Course:BCA\n"
        "Academic Year:2024-2025"
        
    )

    assert employee_details("Alice","E10001""IT",55000) == expected_output 