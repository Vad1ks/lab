from main import *
import pytest

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