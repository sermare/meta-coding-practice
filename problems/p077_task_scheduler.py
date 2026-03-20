DESCRIPTION = """Task Scheduler

You are given an array of CPU tasks, each represented by a character, and a cooling
interval n. Each cycle allows completion of one task. Tasks can be completed in any
order, but there's a constraint: identical tasks must be separated by at least n
intervals.

Return the minimum number of intervals the CPU will take to finish all the given
tasks.

Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

Example 2:
    Input: tasks = ["A","C","A","B","D","B"], n = 1
    Output: 6
    Explanation: A possible sequence is: A -> B -> A -> C -> D -> B.

Example 3:
    Input: tasks = ["A","A","A","B","B","B"], n = 3
    Output: 10

Constraints:
    - 1 <= tasks.length <= 10^4
    - tasks[i] is an uppercase English letter.
    - 0 <= n <= 100
"""


def solution(tasks, n):
    return None
