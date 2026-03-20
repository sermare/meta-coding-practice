DESCRIPTION = """
Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

  - Trie()             Initializes the trie object.
  - void insert(word)  Inserts the string word into the trie.
  - bool search(word)  Returns true if the string word is in the trie (i.e.,
                        was inserted before), and false otherwise.
  - bool startsWith(prefix)  Returns true if there is a previously inserted
                              string word that has the prefix prefix, and false
                              otherwise.

Constraints:
  - 1 <= word.length, prefix.length <= 2000
  - word and prefix consist only of lowercase English letters.
  - At most 3 * 10^4 total calls will be made to insert, search, and
    startsWith.

Examples:
  Input:
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
  Output:
    [null, null, true, false, true, null, true]
""".strip()


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        return None

    def startsWith(self, prefix: str) -> bool:
        return None


solution = Trie
