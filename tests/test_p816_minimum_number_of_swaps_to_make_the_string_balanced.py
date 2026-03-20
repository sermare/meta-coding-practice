from problems.p816_minimum_number_of_swaps_to_make_the_string_balanced import solution

TEST_CASES = [
    {
        "description": "One swap: ']['",
        "run": lambda: solution("][]["),
        "expected": 1,
    },
    {
        "description": "Already balanced: []",
        "run": lambda: solution("[]"),
        "expected": 0,
    },
    {
        "description": "Two swaps: ]]][[[",
        "run": lambda: solution("]]][[["),
        "expected": 2,
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": 0,
    },
]
