DESCRIPTION = """Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a
sentence (at least one word and end with a special character '#').

Implement the AutocompleteSystem class:
- AutocompleteSystem(sentences, times): Initializes with historical data.
- input(c): Takes the next character of the input. If c == '#', save the
  current sentence and return an empty list. Otherwise return the top 3
  historical hot sentences that have the same prefix as the part of the
  sentence already typed. Hot degree is the number of times a sentence has
  been typed. If several sentences have the same hot degree, use
  ASCII-code order.

Example:
    Input: sentences = ["i love you","island","iroman","i love leetcode"],
           times = [5,3,2,2]
           input('i') -> ["i love you","island","i love leetcode"]
           input(' ') -> ["i love you","i love leetcode"]
           input('a') -> []
           input('#') -> []
"""


def solution(sentences, times, inputs):
    return None
