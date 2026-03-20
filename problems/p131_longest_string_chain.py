DESCRIPTION = """Longest String Chain

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere
in wordA without changing the order of the other characters to make it equal to wordB.

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1
is a predecessor of word2, word2 is a predecessor of word3, and so on.

Return the length of the longest possible word chain with words chosen from the given list.

Example:
    Input: words = ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 16
- words[i] only consists of lowercase English letters.
"""


def solution(words):
    return None
