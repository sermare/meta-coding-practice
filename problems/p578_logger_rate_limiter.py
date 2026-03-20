DESCRIPTION = """Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at most every 10 seconds (a message printed
at timestamp t will prevent the same message from being printed until timestamp t + 10).

All messages will come in chronological order.

For this problem, given a list of (timestamp, message) pairs, return a list of booleans
indicating whether each message should be printed.

Example:
    Input: logs = [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
    Output: [True, True, False, False, False, True]
"""


def solution(logs):
    return None
