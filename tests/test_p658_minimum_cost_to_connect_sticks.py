from problems.p658_minimum_cost_to_connect_sticks import solution

TEST_CASES = [
    {
        "description": "Three sticks: [2,4,3]",
        "run": lambda: solution([2, 4, 3]),
        "expected": 14,
    },
    {
        "description": "Already one stick",
        "run": lambda: solution([5]),
        "expected": 0,
    },
    {
        "description": "Two sticks: [1,8]",
        "run": lambda: solution([1, 8]),
        "expected": 9,
    },
    {
        "description": "Four equal sticks: [1,1,1,1]",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 8,
    },
    {
        "description": "Five sticks: [3,5,2,1,4]",
        "run": lambda: solution([3, 5, 2, 1, 4]),
        "expected": 33,
    },
]
