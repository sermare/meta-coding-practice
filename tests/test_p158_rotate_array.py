from problems.p158_rotate_array import solution

TEST_CASES = [
    {
        "description": "Rotate [1..7] by 3",
        "run": lambda: solution([1, 2, 3, 4, 5, 6, 7], 3),
        "expected": [5, 6, 7, 1, 2, 3, 4],
    },
    {
        "description": "Rotate [-1,-100,3,99] by 2",
        "run": lambda: solution([-1, -100, 3, 99], 2),
        "expected": [3, 99, -1, -100],
    },
    {
        "description": "k=0, no rotation",
        "run": lambda: solution([1, 2, 3], 0),
        "expected": [1, 2, 3],
    },
    {
        "description": "k equals length",
        "run": lambda: solution([1, 2, 3], 3),
        "expected": [1, 2, 3],
    },
    {
        "description": "k larger than length",
        "run": lambda: solution([1, 2], 5),
        "expected": [2, 1],
    },
]
