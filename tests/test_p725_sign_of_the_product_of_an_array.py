from problems.p725_sign_of_the_product_of_an_array import solution

TEST_CASES = [
    {
        "description": "Positive product: [-1,-2,-3,-4,3,2,1]",
        "run": lambda: solution([-1, -2, -3, -4, 3, 2, 1]),
        "expected": 1,
    },
    {
        "description": "Negative product: [1,5,0,2,-3]",
        "run": lambda: solution([1, 5, 0, 2, -3]),
        "expected": 0,
    },
    {
        "description": "Negative product: [-1,1,-1,1,-1]",
        "run": lambda: solution([-1, 1, -1, 1, -1]),
        "expected": -1,
    },
    {
        "description": "Single positive: [5]",
        "run": lambda: solution([5]),
        "expected": 1,
    },
    {
        "description": "Contains zero: [0]",
        "run": lambda: solution([0]),
        "expected": 0,
    },
]
