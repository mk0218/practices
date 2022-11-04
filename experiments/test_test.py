import pytest


@pytest.fixture
def test_fixture():
    assert True
    return 1


def test_test(test_fixture):
    assert test_fixture == 1
