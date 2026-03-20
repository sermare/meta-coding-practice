from problems.p628_product_of_array_except_self import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": [24, 12, 8, 6],
    },
    {
        "description": "Contains zero: [-1,1,0,-3,3]",
        "run": lambda: solution([-1, 1, 0, -3, 3]),
        "expected": [0, 0, 9, 0, 0],
    },
    {
        "description": "Two elements: [2,3]",
        "run": lambda: solution([2, 3]),
        "expected": [3, 2],
    },
    {
        "description": "All ones: [1,1,1,1]",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": [1, 1, 1, 1],
    },
]
