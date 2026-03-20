DESCRIPTION = """Car Fleet

There are n cars going to the same destination along a one-lane road. The
destination is target miles away.

You are given two integer arrays position and speed, both of length n, where
position[i] is the position of the ith car and speed[i] is the speed of the
ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and
drive bumper to bumper at the same speed. The faster car will slow down to
match the slower car's speed.

A car fleet is some non-empty set of cars driving at the same speed. Note
that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it is
still considered part of that fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3

Example 2:
    Input: target = 10, position = [3], speed = [3]
    Output: 1

Example 3:
    Input: target = 100, position = [0,2,4], speed = [4,2,1]
    Output: 1

Constraints:
    - n == position.length == speed.length
    - 1 <= n <= 10^5
    - 0 < target <= 10^6
    - 0 <= position[i] < target
    - 0 < speed[i] <= 10^6
"""

def solution(target, position, speed):
    return None
