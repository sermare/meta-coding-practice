from problems.p800_count_number_of_ways_to_place_houses import solution

TEST_CASES = [
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": 4,
    },
    {
        "description": "n=2",
        "run": lambda: solution(2),
        "expected": 9,
    },
    {
        "description": "n=3",
        "run": lambda: solution(3),
        "expected": 25,
    },
    {
        "description": "n=4",
        "run": lambda: solution(4),
        "expected": 64,
    },
]
