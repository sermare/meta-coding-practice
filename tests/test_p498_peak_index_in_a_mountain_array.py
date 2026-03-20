from problems.p498_peak_index_in_a_mountain_array import solution

TEST_CASES = [
    {
        "description": "Simple: [0,1,0] -> 1",
        "run": lambda: solution([0,1,0]),
        "expected": 1,
    },
    {
        "description": "Four elements: [0,2,1,0] -> 1",
        "run": lambda: solution([0,2,1,0]),
        "expected": 1,
    },
    {
        "description": "[0,10,5,2] -> 1",
        "run": lambda: solution([0,10,5,2]),
        "expected": 1,
    },
    {
        "description": "Peak in middle: [1,3,5,4,2] -> 2",
        "run": lambda: solution([1,3,5,4,2]),
        "expected": 2,
    },
    {
        "description": "Peak near end: [1,2,3,4,2] -> 3",
        "run": lambda: solution([1,2,3,4,2]),
        "expected": 3,
    },
]
