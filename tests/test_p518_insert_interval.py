from problems.p518_insert_interval import solution

TEST_CASES = [
    {
        "description": "Basic merge",
        "run": lambda: solution([[1,3],[6,9]], [2,5]),
        "expected": [[1, 5], [6, 9]],
    },
    {
        "description": "Multiple merge",
        "run": lambda: solution([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
        "expected": [[1, 2], [3, 10], [12, 16]],
    },
    {
        "description": "No overlap left",
        "run": lambda: solution([[2,5],[6,9]], [0,1]),
        "expected": [[0, 1], [2, 5], [6, 9]],
    },
    {
        "description": "No overlap right",
        "run": lambda: solution([[1,3],[6,9]], [10,12]),
        "expected": [[1, 3], [6, 9], [10, 12]],
    },
    {
        "description": "Empty intervals",
        "run": lambda: solution([], [1,5]),
        "expected": [[1, 5]],
    },
]
