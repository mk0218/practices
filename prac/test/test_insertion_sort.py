import pytest
from insertion_sort import insertion_sort
from random import shuffle


@pytest.fixture(scope="class")
def fetch_cases_from_file():
    with open("testcase.txt", "r") as f:
        # print(testcases.readline())
        # return testcases
        return f.readlines()


@pytest.fixture
def testcase(fetch_cases_from_file):
    print("HELLO")
    ss = fetch_cases_from_file.split("\n")
    # ss = fetch_cases_from_file.readline().split()
    print(ss)
    # return next(fetch_cases_from_file)
    return str(ss)


@pytest.fixture
def make_random_list():
    src = [i for i in range(1, 101)]
    dst = src[:]
    shuffle(src)
    return (src, dst)


def test_any():
    assert (True)


def test_sorted_asc_list():
    src = [1, 2, 3, 4, 5]
    dst = [1, 2, 3, 4, 5]
    insertion_sort(src)
    assert src == dst


def test_sorted_dsc_list():
    src = [5, 4, 3, 2, 1]
    dst = [1, 2, 3, 4, 5]
    insertion_sort(src)
    assert src == dst


def test_sort_random(make_random_list):
    src, dst = make_random_list
    insertion_sort(src)
    assert src == dst


class TestFromFiles:

    def test_from_file_1(testcase):
        print("!!1!!")
        print(str(testcase))

    def test_from_file_2(testcase):
        print("!!2!!")
        print(testcase)

    def test_from_file_3(testcase):
        print("!!3!!")
        print(testcase)

    def test_from_file_4(testcase):
        print("!!4!!")
        assert True, str(testcase)
