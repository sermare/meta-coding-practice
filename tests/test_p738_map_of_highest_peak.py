from problems.p738_map_of_highest_peak import solution

TEST_CASES = [
    {
        "description": "Basic case: [[0,1],[0,0]]",
        "run": lambda: solution([[0, 1], [0, 0]]),
        "expected": [[1, 0], [2, 1]],
    },
    {
        "description": "All water: [[1,1],[1,1]]",
        "run": lambda: solution([[1, 1], [1, 1]]),
        "expected": [[0, 0], [0, 0]],
    },
    {
        "description": "Water in corners: [[0,0,1],[0,0,0],[1,0,0]]",
        "run": lambda: solution([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        "expected": [[1, 1, 0], [1, 1, 1], [0, 1, 2]],
    },
    {
        "description": "Single cell water: [[1]]",
        "run": lambda: solution([[1]]),
        "expected": [[0]],
    },
]
