from problems.p749_count_common_words_with_one_occurrence import solution

TEST_CASES = [
    {
        "description": "Two common: words1=['leetcode','is','amazing','as','is'], words2=['amazing','leetcode','is']",
        "run": lambda: solution(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]),
        "expected": 2,
    },
    {
        "description": "Three common: words1=['b','bb','bbb'], words2=['a','aa','aaa']",
        "run": lambda: solution(["b", "bb", "bbb"], ["a", "aa", "aaa"]),
        "expected": 0,
    },
    {
        "description": "All common: words1=['a','ab'], words2=['a','a','a','ab']",
        "run": lambda: solution(["a", "ab"], ["a", "a", "a", "ab"]),
        "expected": 1,
    },
    {
        "description": "Empty arrays",
        "run": lambda: solution([], []),
        "expected": 0,
    },
]
