DESCRIPTION = """Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches
any previously added string.

Implement the WordDictionary class:
- WordDictionary() initializes the object.
- addWord(word) adds word to the data structure.
- search(word) returns True if there is any string in the data structure that matches
  word or False otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
    Input:
        WordDictionary wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        wd.search("pad") -> False
        wd.search("bad") -> True
        wd.search(".ad") -> True
        wd.search("b..") -> True

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consists of '.' or lowercase English letters.
- There will be at most 3 dots in word for search queries.
"""


class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word):
        pass

    def search(self, word):
        return None


def solution(operations, arguments):
    """
    operations: list of strings like ["WordDictionary","addWord","search",...]
    arguments: list of lists like [[],["bad"],["b.."]]
    Returns list of results (None for void operations).
    """
    return None
