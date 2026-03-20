from problems.p750_find_target_indices_after_sorting_array import solution

TEST_CASES = [
    {
        "description": "Basic case: nums=[1,2,5,2,3], target=2",
        "run": lambda: solution([1, 2, 5, 2, 3], 2),
        "expected": [1, 2],
    },
    {
        "description": "Target not found: nums=[1,2,5,2,3], target=4",
        "run": lambda: solution([1, 2, 5, 2, 3], 4),
        "expected": [],
    },
    {
        "description": "All same target: nums=[3,3,3], target=3",
        "run": lambda: solution([3, 3, 3], 3),
        "expected": [0, 1, 2],
    },
    {
        "description": "Single element match: nums=[1], target=1",
        "run": lambda: solution([1], 1),
        "expected": [0],
    },
    {
        "description": "Target at boundaries: nums=[1,2,5,2,3], target=5",
        "run": lambda: solution([1, 2, 5, 2, 3], 5),
        "expected": [4],
    },
]
