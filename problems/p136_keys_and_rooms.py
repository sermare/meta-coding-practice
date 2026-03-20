DESCRIPTION = """Keys and Rooms

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. However, you cannot enter a locked room without
having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number
on it, denoting which room it unlocks, and you can take all of them with you to unlock
the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited
room i, return True if you can visit all the rooms, or False otherwise.

Example:
    Input: rooms = [[1],[2],[3],[]]
    Output: True
    Explanation: Visit room 0 -> get key 1 -> visit room 1 -> get key 2 -> visit room 2
                 -> get key 3 -> visit room 3.

Constraints:
- n == rooms.length
- 2 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique.
"""


def solution(rooms):
    return None
