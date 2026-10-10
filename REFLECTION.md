# Reflection (sample answers)

1. Stack vs. queue.
Use a stack when the most recent item should be handled first, such as the undo history in an editor or the call stack of function calls. Use a queue when fairness matters and the oldest item goes first, such as a print queue or customers waiting in line.

2. Why is `list.pop(0)` a poor queue?
Removing the first element of a Python list forces every remaining element to shift left by one, so each dequeue costs O(n). `collections.deque` removes from the front in O(1).

3. Linked list vs. array-backed list.
A linked list inserts or removes at a known node (and at the front) in O(1) without shifting elements. It is worse at random access: reaching the i-th item takes O(n) because you must walk the chain, and each node carries extra memory for its reference.

4. `two_sum` complexity.
It makes one pass and each dictionary lookup is O(1) on average, so it runs in O(n) time with O(n) extra space. Checking every pair is O(n^2), which becomes very slow for large inputs.
