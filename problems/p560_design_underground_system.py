DESCRIPTION = """Design Underground System

An underground railway system keeps track of customer travel times between different
stations.

Implement the UndergroundSystem class:
- checkIn(id, stationName, t) - a customer checks in at stationName at time t.
- checkOut(id, stationName, t) - a customer checks out from stationName at time t.
- getAverageTime(startStation, endStation) - returns the average time to travel from
  startStation to endStation.

For this problem, given a list of operations and arguments, return results for
getAverageTime operations.

Example:
    Input: ops = ["checkIn","checkIn","checkIn","checkOut","checkOut","checkOut",
                  "getAverageTime"],
           args = [[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],
                   [45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],
                   ["Paradise","Cambridge"]]
    Output: [None,None,None,None,None,None,14.0]
"""


def solution(ops, args):
    return None
