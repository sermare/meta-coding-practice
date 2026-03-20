DESCRIPTION = """LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
    - LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    - int get(int key) Gets the value of the key if the key exists, otherwise returns -1.
    - void put(int key, int value) Updates the value of the key if present, or inserts the
      key if not already present. When the cache reaches its capacity, it should invalidate
      and remove the least frequently used key before inserting a new item. For this problem,
      when there is a tie (two or more keys with the same frequency), the least recently
      used key would be evicted.

The functions get and put must each run in O(1) average time complexity.

Example:
    Input:
        ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
    Output:
        [null,null,null,1,null,-1,3,null,1,3,4]

Constraints:
    - 1 <= capacity <= 10^4
    - 0 <= key <= 10^5
    - 0 <= value <= 10^9
    - At most 2 * 10^5 calls will be made to get and put.
"""

class LFUCache(object):
    def __init__(self, capacity):
        pass

    def get(self, key):
        return -1

    def put(self, key, value):
        pass


def solution(operations, arguments):
    """
    Execute a sequence of operations on the LFU Cache.
    operations: list of strings like ["LFUCache", "put", "get", ...]
    arguments: list of lists like [[2], [1,1], [1], ...]
    Returns list of results.
    """
    return None
