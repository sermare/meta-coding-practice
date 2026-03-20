from problems.p831_count_pairs_whose_sum_is_less_than_target import solution

TEST_CASES = [
    {
        "description": "Basic: [-1,1,2,3,1] target=2",
        "run": lambda: solution([-1,1,2,3,1], 2),
        "expected": 3,
    },
    {
        "description": "No pairs: [5,6,7] target=2",
        "run": lambda: solution([5,6,7], 2),
        "expected": 0,
    },
    {
        "description": "All pairs: [-1,-2,-3] target=0",
        "run": lambda: solution([-1,-2,-3], 0),
        "expected": 3,
    },
    {
        "description": "Two elements: [1,2] target=10",
        "run": lambda: solution([1,2], 10),
        "expected": 1,
    },
]
