from problems.p787_minimum_number_of_steps_to_make_two_strings_anagram_ii import solution

TEST_CASES = [
    {
        "description": "Basic: leetcode vs coats",
        "run": lambda: solution("leetcode", "coats"),
        "expected": 7,
    },
    {
        "description": "Already anagrams: abc vs bca",
        "run": lambda: solution("abc", "bca"),
        "expected": 0,
    },
    {
        "description": "Completely different: aaa vs bbb",
        "run": lambda: solution("aaa", "bbb"),
        "expected": 6,
    },
    {
        "description": "Empty and non-empty",
        "run": lambda: solution("", "abc"),
        "expected": 3,
    },
]
