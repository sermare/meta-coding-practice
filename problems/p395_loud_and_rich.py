DESCRIPTION = """
Loud and Rich

There is a group of n people labeled from 0 to n - 1 where each person has a
different amount of money and a different level of quietness.

You are given an array richer where richer[i] = [ai, bi] indicates that ai has
more money than bi, and an integer array quiet where quiet[i] is the quietness
of the ith person.

Return an integer array answer where answer[x] = y if y is the least quiet
person (i.e., the person y with the smallest value of quiet[y]) among all
people who definitely have equal to or more money than the person x.

Constraints:
- n == quiet.length
- 1 <= n <= 500
- 0 <= quiet[i] < n
- All the values of quiet are unique.
- 0 <= richer.length <= n * (n - 1) / 2
- 0 <= ai, bi < n
- ai != bi
- No duplicate pairs in richer.
- The observations in richer are all logically consistent.

Examples:
  Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
  Output: [5,5,2,5,4,5,6,7]

  Input: richer = [], quiet = [0]
  Output: [0]
"""

def solution(richer, quiet):
    """
    For each person, find the quietest person at least as rich.

    Args:
        richer: List[List[int]], richer relationships.
        quiet: List[int], quietness values.

    Returns:
        A list of integers, answer for each person.
    """
    return None
