from problems.p201_two_sum_ii_-_input_array_is_sorted import solution

TEST_CASES = [
    {
        "description": "Basic case: [2,7,11,15] target=9",
        "run": lambda: solution([2, 7, 11, 15], 9),
        "expected": [1, 2],
    },
    {
        "description": "Middle pair: [2,3,4] target=6",
        "run": lambda: solution([2, 3, 4], 6),
        "expected": [1, 3],
    },
    {
        "description": "Negative numbers: [-1,0] target=-1",
        "run": lambda: solution([-1, 0], -1),
        "expected": [1, 2],
    },
    {
        "description": "Last two elements: [1,2,3,4,4,9,56,90] target=8",
        "run": lambda: solution([1, 2, 3, 4, 4, 9, 56, 90], 8),
        "expected": [4, 5],
    },
    {
        "description": "Large values: [5,25,75] target=100",
        "run": lambda: solution([5, 25, 75], 100),
        "expected": [2, 3],
    },
]
