from problems.p790_count_hills_and_valleys_in_an_array import solution

TEST_CASES = [
    {
        "description": "Basic: [2,4,1,1,6,5]",
        "run": lambda: solution([2,4,1,1,6,5]),
        "expected": 3,
    },
    {
        "description": "No hills or valleys: [6,6,5,5,4,1]",
        "run": lambda: solution([6,6,5,5,4,1]),
        "expected": 0,
    },
    {
        "description": "Single hill: [1,3,1]",
        "run": lambda: solution([1,3,1]),
        "expected": 1,
    },
    {
        "description": "Single valley: [3,1,3]",
        "run": lambda: solution([3,1,3]),
        "expected": 1,
    },
]
