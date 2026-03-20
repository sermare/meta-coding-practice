from problems.p736_find_the_most_competitive_subsequence import solution

TEST_CASES = [
    {
        "description": "Basic case: [3,5,2,6], k=2",
        "run": lambda: solution([3, 5, 2, 6], 2),
        "expected": [2, 6],
    },
    {
        "description": "Already sorted: [1,2,3,4], k=3",
        "run": lambda: solution([1, 2, 3, 4], 3),
        "expected": [1, 2, 3],
    },
    {
        "description": "Full array: [2,4,3,3,5,4,9,6], k=4",
        "run": lambda: solution([2, 4, 3, 3, 5, 4, 9, 6], 4),
        "expected": [2, 3, 3, 4],
    },
    {
        "description": "Single element: [5], k=1",
        "run": lambda: solution([5], 1),
        "expected": [5],
    },
]
