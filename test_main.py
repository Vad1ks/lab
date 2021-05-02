from main import *
import pytest
import random
import statistics


def test_user_count():
    tempuser = User()
    assert User.get_all_users_count() == 8


@pytest.mark.parametrize("test_input, expected",
                         [
                             ((5, 4, 5, 3), 4),
                             ((1, 1, 1, 1, 5, 6), 6),
                             pytest.param((5, 5, 4, 5), 5, marks=pytest.mark.xfail)
                         ]
                         )
def test_add_marks(test_input, expected):
    st = Student()
    st.add_marks(*test_input)
    assert len(st.marks) == expected


@pytest.mark.parametrize("test_input, expected",
                         [
                             ((5, 5, 5, 5), 5),
                             ((5, 4, 3, 2, 1), 3),
                             pytest.param((5, 5, 4, 5), 5, marks=pytest.mark.xfail)
                         ]
                         )
def test_averageMark_student(test_input, expected):
    st = Student()
    st.add_marks(*test_input)
    assert st.get_average_mark() == expected


def test_addStudents_to_group():
    testStudentsGroup = (Student("Vadym"), Student("Viktor"), Student("Olha"))
    g = Group("A")
    g.add_student(*testStudentsGroup)
    assert g.get_students_count() == 3


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
    assert round(statistics.mean(marklist), 4) == round(g.get_average_mark(), 4)


@pytest.mark.parametrize("input_array_of_users, expected",
                         [
                             ((Student(), Student(), Student(), Professor()), 4),
                             ((Student(), Professor()), 2),
                             ((), 0),
                             pytest.param(Student(), 2, marks=pytest.mark.xfail)
                         ]
                         )
def test_addUser_chat(input_array_of_users, expected):
    c = Chat("C")
    c.add_user(*input_array_of_users)
    assert len(c.users) == expected
