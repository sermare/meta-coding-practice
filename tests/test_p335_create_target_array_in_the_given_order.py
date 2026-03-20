from problems.p335_create_target_array_in_the_given_order import solution

TEST_CASES = [
    {
        "description": "Basic: nums=[0,1,2,3,4], index=[0,1,2,2,1]",
        "run": lambda: solution([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]),
        "expected": [0, 4, 1, 3, 2],
    },
    {
        "description": "All at front: [1,2,3], [0,0,0]",
        "run": lambda: solution([1, 2, 3], [0, 0, 0]),
        "expected": [3, 2, 1],
    },
    {
        "description": "Sequential: [1,2,3], [0,1,2]",
        "run": lambda: solution([1, 2, 3], [0, 1, 2]),
        "expected": [1, 2, 3],
    },
    {
        "description": "Single element",
        "run": lambda: solution([5], [0]),
        "expected": [5],
    },
]
