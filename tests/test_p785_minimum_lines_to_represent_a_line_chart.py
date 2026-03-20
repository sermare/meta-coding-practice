from problems.p785_minimum_lines_to_represent_a_line_chart import solution

TEST_CASES = [
    {
        "description": "Basic: 8 points, 3 lines",
        "run": lambda: solution([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]),
        "expected": 3,
    },
    {
        "description": "Straight line: [[1,1],[2,2],[3,3]]",
        "run": lambda: solution([[1,1],[2,2],[3,3]]),
        "expected": 1,
    },
    {
        "description": "Two points: [[1,1],[5,5]]",
        "run": lambda: solution([[1,1],[5,5]]),
        "expected": 1,
    },
    {
        "description": "Single point: [[3,4]]",
        "run": lambda: solution([[3,4]]),
        "expected": 0,
    },
]
