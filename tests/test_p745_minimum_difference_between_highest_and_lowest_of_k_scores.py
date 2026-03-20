from problems.p745_minimum_difference_between_highest_and_lowest_of_k_scores import solution

TEST_CASES = [
    {
        "description": "Single student: [90], k=1",
        "run": lambda: solution([90], 1),
        "expected": 0,
    },
    {
        "description": "Basic case: [9,4,1,7], k=2",
        "run": lambda: solution([9, 4, 1, 7], k=2),
        "expected": 2,
    },
    {
        "description": "All same: [5,5,5,5], k=3",
        "run": lambda: solution([5, 5, 5, 5], 3),
        "expected": 0,
    },
    {
        "description": "Larger k: [1,3,6,10,15], k=4",
        "run": lambda: solution([1, 3, 6, 10, 15], 4),
        "expected": 9,
    },
]
