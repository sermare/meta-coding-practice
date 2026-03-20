from problems.p327_squares_of_a_sorted_array import solution

TEST_CASES = [
    {
        "description": "Mixed: [-4,-1,0,3,10]",
        "run": lambda: solution([-4, -1, 0, 3, 10]),
        "expected": [0, 1, 9, 16, 100],
    },
    {
        "description": "Mixed: [-7,-3,2,3,11]",
        "run": lambda: solution([-7, -3, 2, 3, 11]),
        "expected": [4, 9, 9, 49, 121],
    },
    {
        "description": "All positive: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 4, 9],
    },
    {
        "description": "All negative: [-3,-2,-1]",
        "run": lambda: solution([-3, -2, -1]),
        "expected": [1, 4, 9],
    },
]
