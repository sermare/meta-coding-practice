DESCRIPTION = """Exclusive Time of Functions

On a single-threaded CPU, we execute a program containing n functions. Each
function has a unique ID between 0 and n-1. Function calls are stored in a
call stack.

Given the integer n and a list of logs, where each log is a string with
format "{function_id}:{"start"|"end"}:{timestamp}", return the exclusive
time of each function in an array.

Example:
    Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    Output: [3,4]
    Explanation: Function 0 runs [0,1] and [6,6] = 3 units.
                 Function 1 runs [2,5] = 4 units.
"""


def solution(n, logs):
    return None
