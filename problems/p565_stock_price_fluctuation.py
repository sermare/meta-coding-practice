DESCRIPTION = """Stock Price Fluctuation

You are given a stream of records about a particular stock. Each record contains a
timestamp and the corresponding price of the stock at that timestamp.

Implement the StockPrice class:
- update(timestamp, price) - updates the price at the given timestamp (corrects if
  timestamp already exists).
- current() - returns the latest price.
- maximum() - returns the maximum price.
- minimum() - returns the minimum price.

For this problem, given a list of operations and arguments, return a list of results.

Example:
    Input: ops = ["update","update","current","maximum","update","maximum","update",
                  "minimum"],
           args = [[1,10],[2,5],[],[],[1,3],[],[4,2],[]]
    Output: [None,None,5,10,None,5,None,2]
"""


def solution(ops, args):
    return None
