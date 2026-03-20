DESCRIPTION = """Magnetic Force Between Two Balls

In the universe Earth C-137, Rick discovered a special form of magnetic force
between two balls if they are put in his new invented baskets. Rick has n empty
baskets, the ith basket is at position[i]. Morty has m balls and needs to
distribute the balls into the baskets such that the minimum magnetic force between
any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y
is |x - y|.

Given the integer array position and the integer m. Return the required force.

Example 1:
    Input: position = [1,2,3,4,7], m = 3
    Output: 3
    Explanation: Distributing 3 balls into baskets 1, 4, 7 gives forces of
    [3, 3, 6]. The minimum force is 3.

Example 2:
    Input: position = [5,4,3,2,1,1000000000], m = 2
    Output: 999999999

Constraints:
    - n == position.length
    - 2 <= n <= 10^5
    - 1 <= position[i] <= 10^9
    - All integers in position are distinct.
    - 2 <= m <= position.length
"""

def solution(position, m):
    return None
