DESCRIPTION = """
Problem 17: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise
  return -1.
- void put(int key, int value) Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Examples:
  Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
  Output:
    [None, None, None, 1, None, -1, None, -1, 3, 4]
"""


class LRUCache:
    def __init__(self, capacity):
        """
        Initialize the LRU cache with the given capacity.

        Args:
            capacity: Positive integer, the maximum number of key-value pairs.
        """
        pass

    def get(self, key):
        """
        Return the value of the key if it exists, otherwise return -1.

        Args:
            key: Integer key to look up.

        Returns:
            The value associated with the key, or -1 if not found.
        """
        return None

    def put(self, key, value):
        """
        Insert or update a key-value pair. Evict the LRU key if over capacity.

        Args:
            key: Integer key.
            value: Integer value.
        """
        pass


solution = LRUCache
