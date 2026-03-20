DESCRIPTION = """Random Pick with Weight

You are given a 0-indexed array of positive integers `w` where w[i] describes the
weight of the ith index.

Implement the function pickIndex() which randomly picks an index in the range [0, w.length - 1]
(inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For testing: given w and a large number of trials, verify the distribution is approximately
proportional to the weights.

Example:
    Input: w = [1, 3]
    The probability of picking index 0 is 1/4 and index 1 is 3/4.
"""


def solution(w, num_picks):
    """Return a list of num_picks randomly chosen indices, weighted by w."""
    return None
