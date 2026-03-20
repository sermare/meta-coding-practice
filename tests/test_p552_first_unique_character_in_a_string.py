from problems.p552_first_unique_character_in_a_string import solution

TEST_CASES = [
    {
        "description": "First char unique: leetcode",
        "run": lambda: solution("leetcode"),
        "expected": 0,
    },
    {
        "description": "Middle unique: loveleetcode",
        "run": lambda: solution("loveleetcode"),
        "expected": 2,
    },
    {
        "description": "No unique: aabb",
        "run": lambda: solution("aabb"),
        "expected": -1,
    },
    {
        "description": "Single character",
        "run": lambda: solution("z"),
        "expected": 0,
    },
    {
        "description": "Last char unique: aabbccd",
        "run": lambda: solution("aabbccd"),
        "expected": 6,
    },
]
