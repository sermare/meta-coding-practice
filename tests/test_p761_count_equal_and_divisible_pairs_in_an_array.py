from problems.p761_count_equal_and_divisible_pairs_in_an_array import solution

TEST_CASES = [
    {
        "description": "Basic case: [3,1,2,2,2,1,3], k=2",
        "run": lambda: solution([3,1,2,2,2,1,3], 2),
        "expected": 4,
    },
    {
        "description": "All same: [1,2,3,4], k=1",
        "run": lambda: solution([1,2,3,4], 1),
        "expected": 0,
    },
    {
        "description": "All equal: [1,1,1,1], k=1",
        "run": lambda: solution([1,1,1,1], 1),
        "expected": 6,
    },
    {
        "description": "No divisible pairs: [5,5], k=3",
        "run": lambda: solution([5,5], 3),
        "expected": 0,
    },
]
