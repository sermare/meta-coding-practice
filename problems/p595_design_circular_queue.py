DESCRIPTION = """Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data
structure in which the operations are performed based on FIFO principle, and the last
position is connected back to the first position to make a circle.

Implement the MyCircularQueue class:
- MyCircularQueue(k) initializes the queue with size k.
- enQueue(value) inserts an element. Return True if successful.
- deQueue() deletes an element. Return True if successful.
- Front() gets the front item. Return -1 if the queue is empty.
- Rear() gets the last item. Return -1 if the queue is empty.
- isEmpty() checks whether the queue is empty.
- isFull() checks whether the queue is full.

For this problem, given k and a list of operations and arguments, return the results.

Example:
    Input: k = 3,
           ops = ["enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue",
                  "enQueue","Rear"],
           args = [[1],[2],[3],[4],[],[],[],[4],[]]
    Output: [True,True,True,False,3,True,True,True,4]
"""


def solution(k, ops, args):
    return None
