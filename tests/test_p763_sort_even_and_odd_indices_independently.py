from problems.p763_sort_even_and_odd_indices_independently import solution

TEST_CASES = [
    {
        "description": "Basic: [4,1,2,3]",
        "run": lambda: solution([4,1,2,3]),
        "expected": [2,3,4,1],
    },
    {
        "description": "Already sorted: [2,1]",
        "run": lambda: solution([2,1]),
        "expected": [2,1],
    },
    {
        "description": "Longer array: [4,3,2,1,6,5]",
        "run": lambda: solution([4,3,2,1,6,5]),
        "expected": [2,5,4,3,6,1],
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": [1],
    },
]
