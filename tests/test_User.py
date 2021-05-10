from main import User, Chat
import pytest

@pytest.mark.parametrize("test_input, expected",
                         [
                             (3, 3),
                             (4, 4),
                             (0, 0),
                             pytest.param(4, 5, marks=pytest.mark.xfail)
                         ]
                         )
def test_user_count(test_input, expected):
    [User() for _ in range(test_input)]
    assert User.get_all_users_count() == expected
    User.users = []

def test_write_message():
    u = User()
    c = Chat("test")
    u.write_message("test", "Hello")
    assert len(c.messages) == 1
