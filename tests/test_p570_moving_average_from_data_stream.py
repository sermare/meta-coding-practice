from problems.p570_moving_average_from_data_stream import solution

TEST_CASES = [
    {
        "description": "Window 3, vals [1,10,3,5]",
        "run": lambda: solution(3, [1, 10, 3, 5]),
        "expected": [1.0, 5.5, 4.666666666666667, 6.0],
    },
    {
        "description": "Window 1",
        "run": lambda: solution(1, [5, 10, 15]),
        "expected": [5.0, 10.0, 15.0],
    },
    {
        "description": "Window larger than stream",
        "run": lambda: solution(5, [1, 2]),
        "expected": [1.0, 1.5],
    },
    {
        "description": "Single value",
        "run": lambda: solution(3, [10]),
        "expected": [10.0],
    },
]
