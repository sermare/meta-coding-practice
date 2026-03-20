from problems.p022_kth_largest_element_in_an_array import solution

TEST_CASES = [
    {
        "description": "2nd largest in [3,2,1,5,6,4] is 5",
        "run": lambda: solution([3, 2, 1, 5, 6, 4], 2),
        "expected": 5,
    },
    {
        "description": "4th largest in [3,2,3,1,2,4,5,5,6] is 4",
        "run": lambda: solution([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        "expected": 4,
    },
    {
        "description": "1st largest in single-element array is 1",
        "run": lambda: solution([1], 1),
        "expected": 1,
    },
    {
        "description": "5th largest in descending array [7,6,5,4,3,2,1] is 3",
        "run": lambda: solution([7, 6, 5, 4, 3, 2, 1], 5),
        "expected": 3,
    },
    {
        "description": "1st largest in all-ones array is 1",
        "run": lambda: solution([1, 1, 1, 1], 1),
        "expected": 1,
    },
]
