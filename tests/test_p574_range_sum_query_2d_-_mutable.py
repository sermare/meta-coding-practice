from problems.p574_range_sum_query_2d_-_mutable import solution

TEST_CASES = [
    {
        "description": "Sum then update then sum",
        "run": lambda: solution(
            [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]],
            ["sumRegion", "update", "sumRegion"],
            [[2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
        ),
        "expected": [8, None, 10],
    },
    {
        "description": "Single cell sum",
        "run": lambda: solution(
            [[1, 2], [3, 4]],
            ["sumRegion"],
            [[0, 0, 0, 0]]
        ),
        "expected": [1],
    },
    {
        "description": "Full matrix sum",
        "run": lambda: solution(
            [[1, 2], [3, 4]],
            ["sumRegion"],
            [[0, 0, 1, 1]]
        ),
        "expected": [10],
    },
    {
        "description": "Update and re-sum",
        "run": lambda: solution(
            [[1, 2], [3, 4]],
            ["update", "sumRegion"],
            [[0, 0, 10], [0, 0, 1, 1]]
        ),
        "expected": [None, 19],
    },
]
