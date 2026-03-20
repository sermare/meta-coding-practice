from problems.p822_number_of_ways_to_select_buildings import solution

TEST_CASES = [
    {
        "description": "Mixed: 001101",
        "run": lambda: solution("001101"),
        "expected": 6,
    },
    {
        "description": "All same: 000",
        "run": lambda: solution("000"),
        "expected": 0,
    },
    {
        "description": "Alternating: 010",
        "run": lambda: solution("010"),
        "expected": 1,
    },
    {
        "description": "Longer: 11100",
        "run": lambda: solution("11100"),
        "expected": 2,
    },
]
