DESCRIPTION = """
Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList.
- beginWord does not need to be in wordList.

Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

Examples:
  Input: beginWord = "hit", endWord = "cog",
         wordList = ["hot","dot","dog","lot","log","cog"]
  Output: 5
  Explanation: hit -> hot -> dot -> dog -> cog

  Input: beginWord = "hit", endWord = "cog",
         wordList = ["hot","dot","dog","lot","log"]
  Output: 0
"""

def solution(beginWord, endWord, wordList):
    """
    Find the length of shortest transformation sequence.

    Args:
        beginWord: str, starting word.
        endWord: str, target word.
        wordList: List[str], dictionary of words.

    Returns:
        An integer, length of shortest sequence or 0.
    """
    return None
