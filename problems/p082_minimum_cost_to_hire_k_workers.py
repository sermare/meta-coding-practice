DESCRIPTION = """Minimum Cost to Hire K Workers

There are n workers. You are given two integer arrays `quality` and `wage` where
quality[i] is the quality of the ith worker and wage[i] is the minimum wage
expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k
workers, we must pay them according to the following rules:
    1. Every worker in the paid group must be paid at least their minimum wage
       expectation.
    2. In the group, each worker's pay must be directly proportional to their
       quality. This means if a worker's quality is double another worker's, they
       must be paid double.

Given the integer k, return the least amount of money needed to form a paid group
satisfying the above conditions. Answers within 10^-5 of the actual answer will
be accepted.

Example 1:
    Input: quality = [10,20,5], wage = [70,50,30], k = 2
    Output: 105.00000
    Explanation: We pay 70 to worker 0 and 35 to worker 2.

Example 2:
    Input: quality = [3,1,10,10,1], wage = [4,8,2,5,6], k = 3
    Output: 30.66667

Constraints:
    - n == quality.length == wage.length
    - 1 <= k <= n <= 10^4
    - 1 <= quality[i], wage[i] <= 10^4
"""


def solution(quality, wage, k):
    return None
