from problems.p753_richest_customer_wealth import solution

TEST_CASES = [
    {
        "description": "Equal wealth: [[1,2,3],[3,2,1]]",
        "run": lambda: solution([[1,2,3],[3,2,1]]),
        "expected": 6,
    },
    {
        "description": "Different wealth: [[1,5],[7,3],[3,5]]",
        "run": lambda: solution([[1,5],[7,3],[3,5]]),
        "expected": 10,
    },
    {
        "description": "Single customer: [[2,8,7]]",
        "run": lambda: solution([[2,8,7]]),
        "expected": 17,
    },
    {
        "description": "Single bank: [[1],[2],[3]]",
        "run": lambda: solution([[1],[2],[3]]),
        "expected": 3,
    },
]
