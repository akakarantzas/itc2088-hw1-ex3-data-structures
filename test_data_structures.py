"""Tests for Homework 1, Exercise 3. Run with: pytest -v"""

import pytest

import data_structures as ds

Stack, Queue, LinkedList = ds.Stack, ds.Queue, ds.LinkedList


# --- Part 1: Stack ---------------------------------------------------------
def test_stack_lifo_order():
    s = Stack()
    for n in (1, 2, 3):
        s.push(n)
    assert s.size() == 3
    assert s.peek() == 3
    assert [s.pop(), s.pop(), s.pop()] == [3, 2, 1]
    assert s.is_empty()


def test_stack_empty_errors():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()


# --- Part 2: Queue ---------------------------------------------------------
def test_queue_fifo_order():
    q = Queue()
    for n in (1, 2, 3):
        q.enqueue(n)
    assert q.size() == 3
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [1, 2, 3]
    assert q.is_empty()


def test_queue_empty_error():
    with pytest.raises(IndexError):
        Queue().dequeue()


# --- Part 3: LinkedList ----------------------------------------------------
def test_linked_list_append_prepend():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.prepend(1)
    assert ll.to_list() == [1, 2, 3]
    assert len(ll) == 3


def test_linked_list_remove():
    ll = LinkedList()
    for n in (1, 2, 3, 2):
        ll.append(n)
    assert ll.remove(2) is True       # first 2 only
    assert ll.to_list() == [1, 3, 2]
    assert ll.remove(1) is True       # head
    assert ll.to_list() == [3, 2]
    assert ll.remove(99) is False
    assert len(ll) == 2


def test_linked_list_reverse():
    ll = LinkedList()
    for n in (1, 2, 3, 4):
        ll.append(n)
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]
    empty = LinkedList()
    empty.reverse()
    assert empty.to_list() == []


# --- Part 4: Applications --------------------------------------------------
@pytest.mark.parametrize(
    "text, expected",
    [
        ("", True),
        ("()", True),
        ("([]{})", True),
        ("def f(x): return [x, {1: 2}]", True),
        ("(]", False),
        ("(()", False),
        ("())", False),
        ("{[}]", False),
    ],
)
def test_is_balanced(text, expected):
    assert ds.is_balanced(text) is expected


def test_word_frequencies():
    text = "The cat and the hat. The END, the end!"
    assert ds.word_frequencies(text) == {
        "the": 4, "cat": 1, "and": 1, "hat": 1, "end": 2,
    }
    assert ds.word_frequencies("") == {}


def test_remove_duplicates_keeps_order():
    assert ds.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert ds.remove_duplicates([]) == []


def test_remove_duplicates_does_not_mutate_input():
    data = [1, 1, 2]
    ds.remove_duplicates(data)
    assert data == [1, 1, 2]


def test_two_sum():
    assert ds.two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert ds.two_sum([3, 2, 4], 6) == (1, 2)
    assert ds.two_sum([3, 3], 6) == (0, 1)
    assert ds.two_sum([1, 2, 3], 100) is None


def test_hot_potato():
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    assert ds.hot_potato(names, 7) == "Susan"
    assert ds.hot_potato(["A"], 5) == "A"
