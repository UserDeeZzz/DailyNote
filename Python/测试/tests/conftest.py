import pytest


@pytest.fixture(scope="class")
def a_list():
    print("1"*20)
    yield [1, 2, 3, 44, 5]
    print("2"*20)



