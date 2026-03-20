DESCRIPTION = """Booking Concert Tickets in Groups

A concert hall has n rows numbered from 0 to n - 1, each with m seats numbered
from 0 to m - 1. You need to design a ticketing system that can allocate seats
in the following two ways:

1. gather(k, maxRow) - find the first row from 0 to maxRow that has k consecutive
   empty seats. Return [row, startSeat] or empty list [].
2. scatter(k, maxRow) - allocate k seats across rows 0 to maxRow. Return True if
   allocation is possible, False otherwise.

Implement the BookMyShow class with these two methods.

Example:
    bms = BookMyShow(2, 5) # 2 rows, 5 seats each
    bms.gather(4, 0) -> [0, 0]
    bms.gather(2, 0) -> []
    bms.scatter(5, 1) -> True
    bms.scatter(5, 1) -> False

"""


def solution(n, m, operations):
    return None
