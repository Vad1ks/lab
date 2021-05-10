from main import Group, Student
import pytest
import random
from statistics import mean

@pytest.mark.parametrize("test_input, expected",
                         [
                             ((Student(), Student(), Student()), 3),
                             ((Student(), Student(), Student(), Student()), 4),
                             ((), 0),
                             pytest.param((Student(), Student(), Student(), Student()), 5, marks=pytest.mark.xfail)
                         ]
                         )
def test_addStudents_to_group(test_input, expected):
    g = Group("A")
    g.add_student(*test_input)
    assert g.get_students_count() == expected


def test_averageMark_group():
    g = Group("B")
    marklist = []
    for i in range(5):
        s = Student()
        for j in range(5):
            mark = random.randint(1, 5)
            marklist.append(mark)
            s.add_marks(mark)
        g.add_student(s)
    assert round(mean(marklist), 4) == round(g.get_average_mark(), 4)

