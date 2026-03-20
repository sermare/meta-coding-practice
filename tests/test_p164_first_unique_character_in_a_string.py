from problems.p164_first_unique_character_in_a_string import solution

TEST_CASES = [
    {
        "description": "leetcode -> 0",
        "run": lambda: solution("leetcode"),
        "expected": 0,
    },
    {
        "description": "loveleetcode -> 2",
        "run": lambda: solution("loveleetcode"),
        "expected": 2,
    },
    {
        "description": "aabb -> -1",
        "run": lambda: solution("aabb"),
        "expected": -1,
    },
    {
        "description": "Single char -> 0",
        "run": lambda: solution("z"),
        "expected": 0,
    },
]
