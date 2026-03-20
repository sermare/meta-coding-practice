from problems.p721_sort_array_by_increasing_frequency import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,1,2,2,2,3]",
        "run": lambda: solution([1, 1, 2, 2, 2, 3]),
        "expected": [3, 1, 1, 2, 2, 2],
    },
    {
        "description": "Same frequency sorted decreasing: [2,3,1,3,2]",
        "run": lambda: solution([2, 3, 1, 3, 2]),
        "expected": [1, 3, 3, 2, 2],
    },
    {
        "description": "Negative numbers: [-1,1,-6,4,5,-6,1,4,1]",
        "run": lambda: solution([-1, 1, -6, 4, 5, -6, 1, 4, 1]),
        "expected": [5, -1, 4, 4, -6, -6, 1, 1, 1],
    },
    {
        "description": "All same: [5,5,5]",
        "run": lambda: solution([5, 5, 5]),
        "expected": [5, 5, 5],
    },
]
