DESCRIPTION = """Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
- RandomizedSet() initializes the object.
- insert(val) inserts val if not present, returns True if inserted, False otherwise.
- remove(val) removes val if present, returns True if removed, False otherwise.
- getRandom() returns a random element from the current set of elements. Each element
  must have the same probability of being returned.

You must implement the functions such that each function works in average O(1) time complexity.

Example:
    RandomizedSet rs = new RandomizedSet();
    rs.insert(1);    // True
    rs.remove(2);    // False
    rs.insert(2);    // True
    rs.getRandom();  // 1 or 2 randomly
    rs.remove(1);    // True
    rs.insert(2);    // False
    rs.getRandom();  // 2

Constraints:
- -2^31 <= val <= 2^31 - 1
- At most 2 * 10^5 calls to insert, remove, and getRandom.
- There will be at least one element in the data structure when getRandom is called.
"""


def solution(operations, arguments):
    """
    operations: list of strings like ["RandomizedSet","insert","remove","getRandom",...]
    arguments: list of lists like [[],[1],[2],[]]
    Returns list of results (None for void operations, booleans for insert/remove).
    For getRandom, returns the value gotten.
    """
    return None
