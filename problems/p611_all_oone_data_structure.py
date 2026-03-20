DESCRIPTION = """All O`one Data Structure

Design a data structure to store the strings' count with the ability to
return the strings with minimum and maximum counts.

Implement the AllOne class:
- AllOne(): Initializes the object.
- inc(key): Increments the count of the string key by 1.
- dec(key): Decrements the count of the string key by 1. If the count
  reaches 0, remove it.
- getMaxKey(): Returns one of the keys with the maximal count. If no
  element exists, return "".
- getMinKey(): Returns one of the keys with the minimal count. If no
  element exists, return "".

Each function must run in O(1) average time complexity.

Example:
    Input: ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey"]
           [[],["hello"],["hello"],[],[],["leet"],[]]
    Output: [null,null,null,"hello","hello",null,"hello"]
"""


def solution(operations, arguments):
    return None
