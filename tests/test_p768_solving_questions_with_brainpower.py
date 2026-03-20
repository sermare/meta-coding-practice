from problems.p768_solving_questions_with_brainpower import solution

TEST_CASES = [
    {
        "description": "Basic: [[3,2],[4,3],[4,4],[2,5]]",
        "run": lambda: solution([[3,2],[4,3],[4,4],[2,5]]),
        "expected": 5,
    },
    {
        "description": "All solvable: [[1,1],[2,2],[3,3],[4,4],[5,5]]",
        "run": lambda: solution([[1,1],[2,2],[3,3],[4,4],[5,5]]),
        "expected": 7,
    },
    {
        "description": "Single question: [[10,0]]",
        "run": lambda: solution([[10,0]]),
        "expected": 10,
    },
    {
        "description": "Skip first better: [[1,5],[10,0]]",
        "run": lambda: solution([[1,5],[10,0]]),
        "expected": 10,
    },
]
