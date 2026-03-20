DESCRIPTION = """Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes
(i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may
assume that calls are being made to the system in chronological order (i.e., timestamp
is monotonically increasing). Several hits may arrive at roughly the same time.

Implement the HitCounter class:
- HitCounter() initializes the object.
- hit(timestamp) records a hit that happened at timestamp.
- getHits(timestamp) returns the number of hits in the past 5 minutes from timestamp
  (i.e., the past 300 seconds).

Example:
    Input:
        HitCounter counter = new HitCounter();
        counter.hit(1);
        counter.hit(2);
        counter.hit(3);
        counter.getHits(4);   // returns 3
        counter.hit(300);
        counter.getHits(300); // returns 4
        counter.getHits(301); // returns 3

Constraints:
- 1 <= timestamp <= 2 * 10^9
- All the calls are being made in chronological order.
- At most 300 calls will be made to hit and getHits.
"""


def solution(operations, arguments):
    """
    operations: list of strings like ["HitCounter","hit","hit","getHits",...]
    arguments: list of lists like [[],[1],[2],[4]]
    Returns list of results (None for void operations).
    """
    return None
