from problems.p807_maximum_profit_of_operating_a_centennial_wheel import solution

TEST_CASES = [
    {
        "description": "Basic profitable: [8,3] cost=5 run=6",
        "run": lambda: solution([8, 3], 5, 6),
        "expected": 3,
    },
    {
        "description": "Not profitable: [10,9,6] cost=6 run=25",
        "run": lambda: solution([10, 9, 6], 6, 25),
        "expected": -1,
    },
    {
        "description": "Always profitable: [3,4,0,5,1] cost=1 run=1",
        "run": lambda: solution([3, 4, 0, 5, 1], 1, 1),
        "expected": 7,
    },
    {
        "description": "Single arrival: [10] cost=5 run=6",
        "run": lambda: solution([10], 5, 6),
        "expected": 3,
    },
]
