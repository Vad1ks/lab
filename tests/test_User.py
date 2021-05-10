from main import User
import pytest

@pytest.mark.parametrize("test_input, expected",
                         [
                             (3, 3),
                             (4, 7),
                             (0, 7),
                             pytest.param(4, 5, marks=pytest.mark.xfail)
                         ]
                         )
def test_user_count(test_input, expected):
    [User() for _ in range(test_input)]
    assert User.get_all_users_count() == expected