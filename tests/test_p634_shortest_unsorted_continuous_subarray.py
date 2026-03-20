from problems.p634_shortest_unsorted_continuous_subarray import solution

TEST_CASES = [
    {
        "description": "Unsorted middle: [2,6,4,8,10,9,15]",
        "run": lambda: solution([2, 6, 4, 8, 10, 9, 15]),
        "expected": 5,
    },
    {
        "description": "Already sorted: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 0,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "Reverse sorted: [3,2,1]",
        "run": lambda: solution([3, 2, 1]),
        "expected": 3,
    },
    {
        "description": "Two elements unsorted: [2,1]",
        "run": lambda: solution([2, 1]),
        "expected": 2,
    },
]
