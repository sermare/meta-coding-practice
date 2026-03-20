DESCRIPTION = """
Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order
of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where
the strings in words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return "".
If there are multiple valid orderings, return any of them.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.

Examples:
  Input: words = ["wrt","wrf","er","ett","rftt"]
  Output: "wertf"

  Input: words = ["z","x"]
  Output: "zx"

  Input: words = ["z","x","z"]
  Output: "" (invalid order)
"""

def solution(words):
    """
    Derive the order of letters in the alien language.

    Args:
        words: List[str], sorted words in alien language.

    Returns:
        A string representing the letter order, or "" if invalid.
    """
    return None
