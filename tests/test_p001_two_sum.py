from problems.p001_two_sum import solution

TEST_CASES = [
    {
        "description": "Basic case: [2,7,11,15] target=9",
        "run": lambda: solution([2, 7, 11, 15], 9),
        "expected": [0, 1],
    },
    {
        "description": "Middle indices: [3,2,4] target=6",
        "run": lambda: solution([3, 2, 4], 6),
        "expected": [1, 2],
    },
    {
        "description": "Duplicate values: [3,3] target=6",
        "run": lambda: solution([3, 3], 6),
        "expected": [0, 1],
    },
    {
        "description": "Larger array: [1,2,3,4,5] target=9",
        "run": lambda: solution([1, 2, 3, 4, 5], 9),
        "expected": [3, 4],
    },
    {
        "description": "Negative numbers: [-1,-2,-3,-4,-5] target=-8",
        "run": lambda: solution([-1, -2, -3, -4, -5], -8),
        "expected": [2, 4],
    },
]
