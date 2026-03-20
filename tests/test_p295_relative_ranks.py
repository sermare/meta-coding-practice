from problems.p295_relative_ranks import solution

TEST_CASES = [
    {
        "description": "[5,4,3,2,1] -> medals then ranks",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
    },
    {
        "description": "[10,3,8,9,4] -> correct placement",
        "run": lambda: solution([10, 3, 8, 9, 4]),
        "expected": ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
    },
    {
        "description": "[1] -> ['Gold Medal']",
        "run": lambda: solution([1]),
        "expected": ["Gold Medal"],
    },
    {
        "description": "[2,1] -> ['Gold Medal','Silver Medal']",
        "run": lambda: solution([2, 1]),
        "expected": ["Gold Medal", "Silver Medal"],
    },
]
