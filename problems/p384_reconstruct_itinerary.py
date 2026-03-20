DESCRIPTION = """
Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi]
represent the departure and arrival airports of one flight. Reconstruct the
itinerary in order and return it.

All tickets belong to a man who departs from "JFK", thus, the itinerary must
begin with "JFK". If there are multiple valid itineraries, return the itinerary
that has the smallest lexical order when read as a single string.

You may assume all tickets form at least one valid itinerary. You must use all
tickets once and only once.

Constraints:
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters.
- fromi != toi

Examples:
  Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
  Output: ["JFK","MUC","LHR","SFO","SJC"]

  Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
  Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
"""

def solution(tickets):
    """
    Reconstruct the itinerary from airline tickets.

    Args:
        tickets: List[List[str]], the airline tickets.

    Returns:
        A list of strings, the itinerary.
    """
    return None
