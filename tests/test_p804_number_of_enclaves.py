from problems.p804_number_of_enclaves import solution

TEST_CASES = [
    {
        "description": "3 enclaves: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]",
        "run": lambda: solution([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]),
        "expected": 3,
    },
    {
        "description": "No enclaves: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]",
        "run": lambda: solution([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]),
        "expected": 0,
    },
    {
        "description": "All sea: [[0,0],[0,0]]",
        "run": lambda: solution([[0,0],[0,0]]),
        "expected": 0,
    },
    {
        "description": "All boundary land: [[1,1],[1,1]]",
        "run": lambda: solution([[1,1],[1,1]]),
        "expected": 0,
    },
]
