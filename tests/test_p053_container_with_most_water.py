from problems.p053_container_with_most_water import solution

TEST_CASES = [
    {
        "description": "Standard case: [1,8,6,2,5,4,8,3,7]",
        "run": lambda: solution([1, 8, 6, 2, 5, 4, 8, 3, 7]),
        "expected": 49,
    },
    {
        "description": "Two elements: [1,1]",
        "run": lambda: solution([1, 1]),
        "expected": 1,
    },
    {
        "description": "Decreasing heights: [4,3,2,1,4]",
        "run": lambda: solution([4, 3, 2, 1, 4]),
        "expected": 16,
    },
    {
        "description": "Equal heights: [5,5,5,5]",
        "run": lambda: solution([5, 5, 5, 5]),
        "expected": 15,
    },
]
