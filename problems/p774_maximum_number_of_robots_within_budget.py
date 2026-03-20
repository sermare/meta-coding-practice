DESCRIPTION = """Maximum Number of Robots Within Budget

You have n robots. You are given two 0-indexed integer arrays chargeTimes and
runningCosts, both of length n. The i-th robot costs chargeTimes[i] units to
charge and runningCosts[i] units to run.

The total cost of running k chosen robots is:
max(chargeTimes) + k * sum(runningCosts), where the max and sum are taken over
the k robots.

Return the maximum number of consecutive robots you can run such that the total
cost does not exceed budget.

Example:
    Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
    Output: 3
"""


def solution(chargeTimes, runningCosts, budget):
    return None
