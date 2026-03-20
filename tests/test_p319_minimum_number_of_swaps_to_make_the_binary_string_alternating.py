from problems.p319_minimum_number_of_swaps_to_make_the_binary_string_alternating import solution

TEST_CASES = [
    {
        "description": "Basic: 111000 -> 1",
        "run": lambda: solution("111000"),
        "expected": 1,
    },
    {
        "description": "Already alternating: 010 -> 0",
        "run": lambda: solution("010"),
        "expected": 0,
    },
    {
        "description": "Impossible: 1110",
        "run": lambda: solution("1110"),
        "expected": -1,
    },
    {
        "description": "Single char: 1 -> 0",
        "run": lambda: solution("1"),
        "expected": 0,
    },
]
