from main import *
import pytest

@pytest.mark.parametrize("input_array_of_users, expected",
                         [
                             ((Student(), Student(), Student(), Professor()), 4),
                             ((Student(), Professor()), 2),
                             ((), 0),
                             pytest.param(Student(), 2, marks=pytest.mark.xfail),
                             pytest.param((Student(), Student()), 3, marks=pytest.mark.xfail)
                         ]
                         )
def test_addUser_chat(input_array_of_users, expected):
    c = Chat("C")
    c.add_user(*input_array_of_users)
    assert len(c.users) == expected


@pytest.mark.parametrize("test_input, expected",
                         [
                             (3, 3),
                             (4, 4),
                             (0, 0),
                             pytest.param(4, 5, marks=pytest.mark.xfail)
                         ]
                         )
def test_chat_count(test_input, expected):
    Chat.chatList = []
    [Chat("test") for _ in range(test_input)]
    assert len(Chat.chatList) == expected

