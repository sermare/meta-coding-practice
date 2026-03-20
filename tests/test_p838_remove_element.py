from problems.p838_remove_element import solution

TEST_CASES = [
    {
        "description": "Remove 3 from [3,2,2,3]",
        "run": lambda: solution([3,2,2,3], 3),
        "expected": 2,
    },
    {
        "description": "Remove 2 from [0,1,2,2,3,0,4,2]",
        "run": lambda: solution([0,1,2,2,3,0,4,2], 2),
        "expected": 5,
    },
    {
        "description": "Empty array",
        "run": lambda: solution([], 1),
        "expected": 0,
    },
    {
        "description": "No match: [1,2,3] val=4",
        "run": lambda: solution([1,2,3], 4),
        "expected": 3,
    },
]
