from problems.p489_median_of_two_sorted_arrays import solution

TEST_CASES = [
    {
        "description": "Odd total: [1,3]+[2] -> 2.0",
        "run": lambda: solution([1,3], [2]),
        "expected": 2.0,
    },
    {
        "description": "Even total: [1,2]+[3,4] -> 2.5",
        "run": lambda: solution([1,2], [3,4]),
        "expected": 2.5,
    },
    {
        "description": "One empty: []+[1] -> 1.0",
        "run": lambda: solution([], [1]),
        "expected": 1.0,
    },
    {
        "description": "One empty: [2]+[] -> 2.0",
        "run": lambda: solution([2], []),
        "expected": 2.0,
    },
    {
        "description": "Same arrays: [1,2]+[1,2] -> 1.5",
        "run": lambda: solution([1,2], [1,2]),
        "expected": 1.5,
    },
]
