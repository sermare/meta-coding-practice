DESCRIPTION = """Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for
the same key at different time stamps and retrieve the key's value at a certain
timestamp.

Implement the TimeMap class:
    - TimeMap() Initializes the object.
    - set(key, value, timestamp) Stores the key with the value at the given
      timestamp.
    - get(key, timestamp) Returns a value such that set was called previously, with
      timestamp_prev <= timestamp. If there are multiple such values, it returns
      the value associated with the largest timestamp_prev. If there are no values,
      it returns "".

Example 1:
    Input:
    ["TimeMap", "set", "get", "get", "set", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4]]
    Output: [null, null, "bar", "bar", null, "bar2"]

Constraints:
    - 1 <= key.length, value.length <= 100
    - key and value consist of lowercase English letters and digits.
    - 1 <= timestamp <= 10^7
    - All the timestamps of set are strictly increasing.
    - At most 2 * 10^5 calls will be made to set and get.
"""


def solution(operations, arguments):
    return None
