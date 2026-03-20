DESCRIPTION = """Furthest Building You Can Reach

You are given an integer array heights representing the heights of buildings, some
bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using
bricks or ladders.

While moving from building i to building i+1 (0-indexed):
- If the current building's height is >= next building's height, no ladder or bricks needed.
- If the current building's height < next building's height, you can either use
  (h[i+1] - h[i]) bricks or one ladder.

Return the furthest building index (0-indexed) you can reach if you use the given
ladders and bricks optimally.

Example:
    Input: heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1
    Output: 4
"""


def solution(heights, bricks, ladders):
    return None
