from problems.p350_container_with_most_water import solution

TEST_CASES = [
    {
        "description": "Basic: [1,8,6,2,5,4,8,3,7] -> 49",
        "run": lambda: solution([1, 8, 6, 2, 5, 4, 8, 3, 7]),
        "expected": 49,
    },
    {
        "description": "Two elements: [1,1] -> 1",
        "run": lambda: solution([1, 1]),
        "expected": 1,
    },
    {
        "description": "Decreasing: [5,4,3,2,1] -> 6",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": 6,
    },
    {
        "description": "All same: [3,3,3,3] -> 9",
        "run": lambda: solution([3, 3, 3, 3]),
        "expected": 9,
    },
]
