DESCRIPTION = """Minimum Difficulty of a Job Schedule

You want to schedule a list of jobs in d days. Jobs are dependent (i.e., to work on the
i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a day is the maximum
difficulty of a job done on that day. The difficulty of a job schedule is the sum of
difficulties of each day.

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the
jobs return -1.

Example:
    Input: jobDifficulty = [6,5,4,3,2,1], d = 2
    Output: 7
    Explanation: Day 1: [6,5,4,3,2] difficulty=6. Day 2: [1] difficulty=1. Total=7.

Constraints:
- 1 <= jobDifficulty.length <= 300
- 0 <= jobDifficulty[i] <= 1000
- 1 <= d <= 10
"""


def solution(jobDifficulty, d):
    return None
