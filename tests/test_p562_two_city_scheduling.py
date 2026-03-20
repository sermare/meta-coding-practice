from problems.p562_two_city_scheduling import solution

TEST_CASES = [
    {
        "description": "Four people: 110",
        "run": lambda: solution([[10, 20], [30, 200], [400, 50], [30, 20]]),
        "expected": 110,
    },
    {
        "description": "Six people: 1859",
        "run": lambda: solution([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]),
        "expected": 1859,
    },
    {
        "description": "Two people",
        "run": lambda: solution([[1, 100], [100, 1]]),
        "expected": 2,
    },
    {
        "description": "Equal costs",
        "run": lambda: solution([[10, 10], [10, 10]]),
        "expected": 20,
    },
]
