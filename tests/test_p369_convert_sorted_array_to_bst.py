from problems.p369_convert_sorted_array_to_bst import solution


TEST_CASES = [
    {
        "description": "Five elements",
        "run": lambda: solution([-10, -3, 0, 5, 9]),
        "expected": [-10, -3, 0, 5, 9],
    },
    {
        "description": "Two elements",
        "run": lambda: solution([1, 3]),
        "expected": [1, 3],
    },
    {
        "description": "Single element",
        "run": lambda: solution([0]),
        "expected": [0],
    },
    {
        "description": "Four elements",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": [1, 2, 3, 4],
    },
]
