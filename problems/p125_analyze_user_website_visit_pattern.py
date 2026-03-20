DESCRIPTION = """Analyze User Website Visit Pattern

You are given two string arrays username and website and an integer array timestamp.
All the arrays are of the same length and the tuple [username[i], website[i], timestamp[i]]
indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

A 3-sequence is a pattern where the visits happen in chronological order.

The score of a pattern is the number of users that visited all the websites in the pattern
in the same order (not necessarily consecutively).

Return the pattern with the largest score. If there is more than one pattern with the same
largest score, return the lexicographically smallest such pattern.

Example:
    Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
           timestamp = [1,2,3,4,5,6,7,8,9,10],
           website = ["home","about","career","home","cart","maps","home","home","about","career"]
    Output: ["home","about","career"]

Constraints:
- 3 <= username.length <= 50
- 1 <= username[i].length <= 10
- timestamp[i] is a positive integer in [1, 10^9]
- 1 <= website[i].length <= 10
"""


def solution(username, timestamp, website):
    return None
