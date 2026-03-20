from problems.p587_merge_two_sorted_lists import solution

TEST_CASES = [
    {
        "description": "Standard merge: [1,2,4] + [1,3,4]",
        "run": lambda: solution([1, 2, 4], [1, 3, 4]),
        "expected": [1, 1, 2, 3, 4, 4],
    },
    {
        "description": "Both empty",
        "run": lambda: solution([], []),
        "expected": [],
    },
    {
        "description": "One empty: [] + [0]",
        "run": lambda: solution([], [0]),
        "expected": [0],
    },
    {
        "description": "No overlap: [1,2] + [3,4]",
        "run": lambda: solution([1, 2], [3, 4]),
        "expected": [1, 2, 3, 4],
    },
    {
        "description": "Single elements: [5] + [1]",
        "run": lambda: solution([5], [1]),
        "expected": [1, 5],
    },
]
