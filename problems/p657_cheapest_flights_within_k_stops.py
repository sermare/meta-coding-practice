DESCRIPTION = """Cheapest Flights Within K Stops

There are `n` cities connected by some number of flights. You are given an array
`flights` where flights[i] = [from_i, to_i, price_i] indicates a flight from city
from_i to city to_i with cost price_i.

Given `src`, `dst`, and `k`, return the cheapest price from src to dst with at most
k stops. If there is no such route, return -1.

Example:
    Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
           src = 0, dst = 3, k = 1
    Output: 700
    Explanation: The optimal path is 0 -> 1 -> 3 with cost 100 + 600 = 700.
"""


def solution(n, flights, src, dst, k):
    return None
