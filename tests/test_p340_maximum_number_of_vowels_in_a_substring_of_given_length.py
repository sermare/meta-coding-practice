from problems.p340_maximum_number_of_vowels_in_a_substring_of_given_length import solution

TEST_CASES = [
    {
        "description": "Basic: abciiidef k=3 -> 3",
        "run": lambda: solution("abciiidef", 3),
        "expected": 3,
    },
    {
        "description": "Mixed: aeiou k=2 -> 2",
        "run": lambda: solution("aeiou", 2),
        "expected": 2,
    },
    {
        "description": "No vowels: bcdfg k=2 -> 0",
        "run": lambda: solution("bcdfg", 2),
        "expected": 0,
    },
    {
        "description": "leetcode k=3 -> 2",
        "run": lambda: solution("leetcode", 3),
        "expected": 2,
    },
]
