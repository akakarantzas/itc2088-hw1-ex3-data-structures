# Homework 1, Exercise 3: Data Structures

**Course:** Introduction to Programming
**Term:** Academic Year 2023-2024 - Spring
**Language:** Python 3.9+
**Total:** 100 points

## Overview

In this homework you will build three classic data structures from scratch (stack, queue, linked list) and then use them, along with Python's built-in `dict` and `set`, to solve small practical problems.

## Learning objectives

- Explain the difference between LIFO (stack) and FIFO (queue) behavior.
- Implement a linked list using nodes and references.
- Choose an appropriate data structure for a problem.
- Use dictionaries and sets for counting, lookup, and de-duplication.
- Test your code with automated tests.

## Getting started

1. Open `data_structures.py`.
2. Implement each class and function. Do not rename anything.
3. Run the tests against your work:

   ```bash
   pip install pytest
   pytest -v
   ```


## Tasks

### Part 1: Stack (15 points)

Implement `Stack` with `push`, `pop`, `peek`, `is_empty`, and `size`. `pop` and `peek` must raise `IndexError` on an empty stack.

### Part 2: Queue (15 points)

Implement `Queue` with `enqueue`, `dequeue`, `is_empty`, and `size`. `dequeue` must raise `IndexError` on an empty queue.

### Part 3: Linked list (25 points)

Implement `LinkedList` using `Node` objects. You may **not** store the items in a Python list.

| Method | Behavior |
| --- | --- |
| `append(value)` | add to the end |
| `prepend(value)` | add to the front |
| `remove(value)` | remove the first match; return `True`/`False` |
| `reverse()` | reverse in place by re-pointing `next` links |
| `to_list()` | return values as a Python list |
| `len(ll)` | number of nodes |

### Part 4: Applications (35 points)

| Function | Points | Description |
| --- | --- | --- |
| `is_balanced(text)` | 10 | Check `()`, `[]`, `{}` nesting. **Must use your `Stack`.** |
| `word_frequencies(text)` | 7 | Case-insensitive word counts using a `dict`. |
| `remove_duplicates(items)` | 6 | Remove duplicates, keep order, use a `set`. |
| `two_sum(numbers, target)` | 7 | Return indices of two numbers adding to `target` in one pass. |
| `hot_potato(names, num)` | 5 | Elimination game. **Must use your `Queue`.** |

### Part 5: Reflection (10 points)

Add a file `REFLECTION.md` with short answers (2-4 sentences each):

1. When would you pick a stack over a queue? Give a real-world example of each.
2. Why is `list.pop(0)` a poor choice for a queue?
3. What does a linked list do better than an array-backed list? What does it do worse?
4. What is the time complexity of your `two_sum`, and why is it better than checking every pair?

## Grading

| Part | Points |
| --- | --- |
| 1. Stack | 15 |
| 2. Queue | 15 |
| 3. Linked list | 25 |
| 4. Applications | 35 |
| 5. Reflection | 10 |

Parts 1-4 are graded by the automated tests plus a quick read for the "must use" constraints. Clean, readable code with docstrings and sensible names is expected.

## Submission

Push your completed `data_structures.py` and `REFLECTION.md` to your repository and submit the link.

## Academic integrity

