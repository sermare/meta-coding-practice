DESCRIPTION = """Minimum Speed to Arrive on Time

You are given a floating-point number hour, representing the amount of time you
have to reach the office. To commute to the office, you must take n trains in
sequential order. You are also given an integer array dist of length n, where
dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between
each train ride.

Return the minimum positive integer speed (in kilometers per hour) that all the
trains must travel at for you to reach the office on time, or -1 if it is impossible
to be on time.

Tests are generated such that the answer will not exceed 10^7.

Example 1:
    Input: dist = [1,3,2], hour = 6
    Output: 1

Example 2:
    Input: dist = [1,3,2], hour = 2.7
    Output: 3

Example 3:
    Input: dist = [1,3,2], hour = 1.9
    Output: -1

Constraints:
    - n == dist.length
    - 1 <= n <= 10^5
    - 1 <= dist[i] <= 10^5
    - 1 <= hour <= 10^9
"""

def solution(dist, hour):
    return None
