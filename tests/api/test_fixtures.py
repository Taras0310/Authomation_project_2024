import pytest

@pytest.mark.check
def test_change_name(user):

    assert user.name == 'Taras'

@pytest.mark.check
def test_change_second_name(user):

    assert user.second_name == 'Yakushevych'