from problems.p770_longest_subsequence_with_limited_sum import solution

TEST_CASES = [
    {
        "description": "Basic: nums=[4,5,2,1], queries=[3,10,21]",
        "run": lambda: solution([4,5,2,1], [3,10,21]),
        "expected": [2,3,4],
    },
    {
        "description": "Single element: nums=[1], queries=[1,2]",
        "run": lambda: solution([1], [1,2]),
        "expected": [1,1],
    },
    {
        "description": "Query too small: nums=[5,10], queries=[1]",
        "run": lambda: solution([5,10], [1]),
        "expected": [0],
    },
    {
        "description": "Large query: nums=[2,3,4,5], queries=[100]",
        "run": lambda: solution([2,3,4,5], [100]),
        "expected": [4],
    },
]
