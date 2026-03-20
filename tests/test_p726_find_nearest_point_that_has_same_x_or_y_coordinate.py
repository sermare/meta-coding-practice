from problems.p726_find_nearest_point_that_has_same_x_or_y_coordinate import solution

TEST_CASES = [
    {
        "description": "Basic case: x=3, y=4",
        "run": lambda: solution(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]),
        "expected": 2,
    },
    {
        "description": "No valid points: x=3, y=4",
        "run": lambda: solution(3, 4, [[2, 5]]),
        "expected": -1,
    },
    {
        "description": "Exact match: x=1, y=1",
        "run": lambda: solution(1, 1, [[1, 1]]),
        "expected": 0,
    },
    {
        "description": "Multiple same distance: x=3, y=4",
        "run": lambda: solution(3, 4, [[3, 5], [3, 3]]),
        "expected": 0,
    },
]
