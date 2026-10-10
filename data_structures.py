"""ITC 2088 - Homework 1, Exercise 3: Data Structures."""

from collections import deque


# ---------------------------------------------------------------------------
# Part 1: Stack
# ---------------------------------------------------------------------------
class Stack:
    """A last-in, first-out (LIFO) stack backed by a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# ---------------------------------------------------------------------------
# Part 2: Queue
# ---------------------------------------------------------------------------
class Queue:
    """A first-in, first-out (FIFO) queue backed by collections.deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# ---------------------------------------------------------------------------
# Part 3: Singly linked list
# ---------------------------------------------------------------------------
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """Add value to the end of the list."""
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def prepend(self, value):
        """Add value to the front of the list."""
        self.head = Node(value, self.head)
        self._size += 1

    def remove(self, value):
        """Remove the first node holding value. Return True if removed."""
        previous = None
        current = self.head
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next
        return False

    def reverse(self):
        """Reverse the list in place."""
        previous = None
        current = self.head
        while current is not None:
            current.next, previous, current = previous, current, current.next
        self.head = previous

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self._size


# ---------------------------------------------------------------------------
# Part 4: Applications
# ---------------------------------------------------------------------------
def is_balanced(text):
    """Return True if every (), [], {} in text is properly matched and nested."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in text:
        if ch in pairs.values():
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


def word_frequencies(text):
    """Count words, ignoring case and surrounding punctuation."""
    counts = {}
    for raw in text.split():
        word = raw.strip(".,!?;:\"'()[]{}").lower()
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def remove_duplicates(items):
    """Return a new list with duplicates removed, keeping first occurrences."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def two_sum(numbers, target):
    """Return indices (i, j), i < j, with numbers[i] + numbers[j] == target.

    Return None if no such pair exists.
    """
    seen = {}  # value -> index
    for j, n in enumerate(numbers):
        i = seen.get(target - n)
        if i is not None:
            return (i, j)
        seen[n] = j
    return None


def hot_potato(names, num):
    """Josephus-style elimination game using a Queue.

    Players pass the potato num times around the circle; whoever holds it
    is eliminated. Return the name of the last player remaining.
    """
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()
