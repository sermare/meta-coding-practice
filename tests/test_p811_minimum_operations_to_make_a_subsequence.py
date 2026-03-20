from problems.p811_minimum_operations_to_make_a_subsequence import solution

TEST_CASES = [
    {
        "description": "Need 2 insertions: target=[5,1,3] arr=[9,4,2,3,4]",
        "run": lambda: solution([5,1,3], [9,4,2,3,4]),
        "expected": 2,
    },
    {
        "description": "Already subsequence: target=[1,2,3] arr=[1,2,3,4]",
        "run": lambda: solution([1,2,3], [1,2,3,4]),
        "expected": 0,
    },
    {
        "description": "No overlap: target=[1,2] arr=[3,4]",
        "run": lambda: solution([1,2], [3,4]),
        "expected": 2,
    },
    {
        "description": "Single element: target=[1] arr=[1]",
        "run": lambda: solution([1], [1]),
        "expected": 0,
    },
]
