DESCRIPTION = """All O`one Data Structure

Design a data structure to store the strings' count with the ability to return the
strings with minimum and maximum counts.

Implement the AllOne class:
- AllOne() initializes the object.
- inc(key) increments the count of the string key by 1. If key does not exist, insert
  it with count 1.
- dec(key) decrements the count of the string key by 1. If the count of key is 0 after
  the decrement, remove it.
- getMaxKey() returns one of the keys with the maximal count. If no element exists,
  return "".
- getMinKey() returns one of the keys with the minimal count. If no element exists,
  return "".

For this problem, given a list of operations and arguments, return a list of results
for getMaxKey and getMinKey operations.

Example:
    Input: ops = ["inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"],
           args = [["hello"],["hello"],[],[],["leet"],[],[]]
    Output: [None,None,"hello","hello",None,"hello","leet"]
"""


def solution(ops, args):
    return None
