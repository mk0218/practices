import pytest
from priority_queue import *


@pytest.fixture(name="pq")
def create():
    return PriorityQueue()


@pytest.fixture(name="pq_desc")
def create_descending():
    return PriorityQueue(descending=True)


@pytest.fixture(name="maxpq")
def create_maxpq():
    return MaxPriorityQueue()


def test_min_priority_queue(pq):
    testcase = [-1, 5, 2, 3, 4, -2, -4, -5, 0, -3, 1]
    expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    for value in testcase:
        pq.push(value)
    result = []
    while True:
        try:
            result.append(pq.pop())
        except IndexError:
            break
    assert result == expected


def test_max_priority_queue(maxpq):
    testcase = [-1, 5, 2, 3, 4, -2, -4, -5, 0, -3, 1]
    expected = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
    for value in testcase:
        maxpq.push(value)
    result = []
    while True:
        try:
            result.append(maxpq.pop())
        except IndexError:
            break
    assert result == expected


def test_priority_queue_min(pq):
    testcase = [-1, 5, 2, 3, 4, -2, -4, -5, 0, -3, 1]
    expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    for value in testcase:
        pq.push(value)
    result = []
    while True:
        try:
            result.append(pq.pop())
        except IndexError:
            break
    assert result == expected


def test_priority_queue_max(pq_desc):
    testcase = [-1, 5, 2, 3, 4, -2, -4, -5, 0, -3, 1]
    expected = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
    for value in testcase:
        pq_desc.push(value)
    result = []
    while True:
        try:
            result.append(pq_desc.pop())
        except IndexError:
            break
    assert result == expected