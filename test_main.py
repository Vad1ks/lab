from main import *
import pytest


def test_user_count():
    tempuser = User()
    assert User.get_all_users_count() == 1


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
