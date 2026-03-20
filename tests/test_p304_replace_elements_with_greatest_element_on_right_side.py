from problems.p304_replace_elements_with_greatest_element_on_right_side import solution

TEST_CASES = [
    {
        "description": "Basic case: [17,18,5,4,6,1]",
        "run": lambda: solution([17, 18, 5, 4, 6, 1]),
        "expected": [18, 6, 6, 6, 1, -1],
    },
    {
        "description": "Single element",
        "run": lambda: solution([400]),
        "expected": [-1],
    },
    {
        "description": "Ascending array",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": [4, 4, 4, -1],
    },
    {
        "description": "Descending array",
        "run": lambda: solution([4, 3, 2, 1]),
        "expected": [3, 2, 1, -1],
    },
]
