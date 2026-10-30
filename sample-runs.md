Sample Runs: Stacks and Queues

1. Array Stack

Operations:

1. Push 10.
2. Push 20.
3. Peek.
4. Pop.

Expected results:

Top item: 20
Popped: 20
Current state: Stack: [10]

2. Stack Underflow

Attempt to pop from an empty stack.

Expected error:

Stack underflow: stack is empty.

3. Array Stack Overflow

With a capacity of 5, attempt to push a sixth item without removing an existing item.

Expected error:

Stack overflow: stack is full.

4. Array Queue

Operations:

1. Enqueue A.
2. Enqueue B.
3. Dequeue.
4. Enqueue C.

Expected results:

Dequeued: A
Current queue: [B, C]

5. Queue Underflow

Attempt to dequeue from an empty queue.

Expected error:

Queue underflow: queue is empty.

6. Queue Overflow

With a capacity of 5, attempt to enqueue a sixth item without dequeuing an existing item.

Expected error:

Queue overflow: queue is full.

Testing Note

These are expected example results. Actual output should be verified by running the program in Python.
