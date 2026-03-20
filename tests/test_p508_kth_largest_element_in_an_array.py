from problems.p508_kth_largest_element_in_an_array import solution

TEST_CASES = [
    {
        "description": "Basic case k=2",
        "run": lambda: solution([3,2,1,5,6,4], 2),
        "expected": 5,
    },
    {
        "description": "k=4 with duplicates",
        "run": lambda: solution([3,2,3,1,2,4,5,5,6], 4),
        "expected": 4,
    },
    {
        "description": "k=1 largest",
        "run": lambda: solution([1,2,3], 1),
        "expected": 3,
    },
    {
        "description": "Single element",
        "run": lambda: solution([7], 1),
        "expected": 7,
    },
    {
        "description": "All same elements",
        "run": lambda: solution([5,5,5,5], 2),
        "expected": 5,
    },
]
