DESCRIPTION = """LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU)
cache.

Implement the LRUCache class:
- LRUCache(capacity) initializes the LRU cache with positive size capacity.
- get(key) returns the value of the key if the key exists, otherwise returns -1.
- put(key, value) updates the value of the key if present, or inserts the key-value
  pair. When the cache reaches its capacity, it should invalidate the least recently
  used key before inserting a new item.

For this problem, given the capacity, a list of operations, and their arguments, return
the results.

Example:
    Input: capacity = 2,
           ops = ["put","put","get","put","get","put","get","get","get"],
           args = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    Output: [None,None,1,None,-1,None,-1,3,4]
"""


def solution(capacity, ops, args):
    return None
