DESCRIPTION = """
Possible Bipartition

We want to split a group of n people (labeled from 1 to n) into two groups of
any size. Each person may dislike some other people, and they should not go into
the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
indicates that the person ai dislikes person bi, return true if it is possible
to split everyone into two groups this way.

Constraints:
- 1 <= n <= 2000
- 0 <= dislikes.length <= 10^4
- dislikes[i].length == 2
- 1 <= ai < bi <= n
- All the pairs are unique.

Examples:
  Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
  Output: True

  Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
  Output: False

  Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
  Output: False
"""

def solution(n, dislikes):
    """
    Determine if people can be split into two groups.

    Args:
        n: int, number of people.
        dislikes: List[List[int]], dislike pairs.

    Returns:
        Boolean, True if bipartition is possible.
    """
    return None
