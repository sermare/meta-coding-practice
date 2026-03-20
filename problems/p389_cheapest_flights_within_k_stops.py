DESCRIPTION = """
Cheapest Flights Within K Stops

There are n cities connected by some flights. You are given an array flights
where flights[i] = [fromi, toi, pricei] indicates there is a flight from city
fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price
from src to dst with at most k stops. If there is no such route, return -1.

Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1)) / 2
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 10^4
- There are no duplicate flights.
- 0 <= src, dst, k < n
- src != dst

Examples:
  Input: n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1
  Output: 700

  Input: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1
  Output: 200

  Input: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=0
  Output: 500
"""

def solution(n, flights, src, dst, k):
    """
    Find cheapest flight price from src to dst with at most k stops.

    Args:
        n: int, number of cities.
        flights: List[List[int]], flights with prices.
        src: int, source city.
        dst: int, destination city.
        k: int, max number of stops.

    Returns:
        An integer, cheapest price or -1.
    """
    return None
