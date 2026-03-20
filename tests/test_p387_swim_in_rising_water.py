from problems.p387_swim_in_rising_water import solution


TEST_CASES = [
    {
        "description": "2x2 grid: time 3",
        "run": lambda: solution([[0, 2], [1, 3]]),
        "expected": 3,
    },
    {
        "description": "5x5 grid: time 16",
        "run": lambda: solution([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]),
        "expected": 16,
    },
    {
        "description": "1x1 grid: time 0",
        "run": lambda: solution([[0]]),
        "expected": 0,
    },
    {
        "description": "3x3 grid",
        "run": lambda: solution([[0, 1, 2], [5, 4, 3], [6, 7, 8]]),
        "expected": 8,
    },
]
