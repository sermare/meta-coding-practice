from problems.p316_find_the_index_of_the_first_occurrence_in_a_string import solution

TEST_CASES = [
    {
        "description": "Found at start: sadbutsad/sad -> 0",
        "run": lambda: solution("sadbutsad", "sad"),
        "expected": 0,
    },
    {
        "description": "Not found: leetcode/leeto -> -1",
        "run": lambda: solution("leetcode", "leeto"),
        "expected": -1,
    },
    {
        "description": "Found in middle: hello/ll -> 2",
        "run": lambda: solution("hello", "ll"),
        "expected": 2,
    },
    {
        "description": "Exact match: a/a -> 0",
        "run": lambda: solution("a", "a"),
        "expected": 0,
    },
]
