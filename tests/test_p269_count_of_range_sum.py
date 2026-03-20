from problems.p269_count_of_range_sum import solution

TEST_CASES = [
    {
        "description": "[-2,5,-1] lower=-2 upper=2 -> 3",
        "run": lambda: solution([-2, 5, -1], -2, 2),
        "expected": 3,
    },
    {
        "description": "[0] lower=0 upper=0 -> 1",
        "run": lambda: solution([0], 0, 0),
        "expected": 1,
    },
    {
        "description": "[1,2,3] lower=3 upper=6 -> 3",
        "run": lambda: solution([1, 2, 3], 3, 6),
        "expected": 3,
    },
    {
        "description": "[-1] lower=-1 upper=0 -> 1",
        "run": lambda: solution([-1], -1, 0),
        "expected": 1,
    },
    {
        "description": "[0,0] lower=0 upper=0 -> 3",
        "run": lambda: solution([0, 0], 0, 0),
        "expected": 3,
    },
]
