from problems.p226_kth_largest_element_in_a_stream import solution

TEST_CASES = [
    {
        "description": "Standard: k=3, nums=[4,5,8,2]",
        "run": lambda: solution(3, [4, 5, 8, 2], [3, 5, 10, 9, 4]),
        "expected": [4, 5, 5, 8, 8],
    },
    {
        "description": "k=1, always return max",
        "run": lambda: solution(1, [], [1, 2, 3]),
        "expected": [1, 2, 3],
    },
    {
        "description": "k=2, small stream",
        "run": lambda: solution(2, [0], [1, 2, 3]),
        "expected": [0, 1, 2],
    },
    {
        "description": "Duplicates",
        "run": lambda: solution(2, [1, 1], [1, 1]),
        "expected": [1, 1],
    },
]
