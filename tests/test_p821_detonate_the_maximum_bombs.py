from problems.p821_detonate_the_maximum_bombs import solution

TEST_CASES = [
    {
        "description": "Chain: [[2,1,3],[6,1,4]]",
        "run": lambda: solution([[2,1,3],[6,1,4]]),
        "expected": 2,
    },
    {
        "description": "No chain: [[1,1,5],[10,10,5]]",
        "run": lambda: solution([[1,1,5],[10,10,5]]),
        "expected": 1,
    },
    {
        "description": "All connected: [[1,1,100],[2,2,100],[3,3,100]]",
        "run": lambda: solution([[1,1,100],[2,2,100],[3,3,100]]),
        "expected": 3,
    },
    {
        "description": "Single bomb: [[0,0,1]]",
        "run": lambda: solution([[0,0,1]]),
        "expected": 1,
    },
]
