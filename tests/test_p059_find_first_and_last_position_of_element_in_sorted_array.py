from problems.p059_find_first_and_last_position_of_element_in_sorted_array import solution

TEST_CASES = [
    {
        "description": "Target found: [5,7,7,8,8,10] target=8",
        "run": lambda: solution([5, 7, 7, 8, 8, 10], 8),
        "expected": [3, 4],
    },
    {
        "description": "Target not found: [5,7,7,8,8,10] target=6",
        "run": lambda: solution([5, 7, 7, 8, 8, 10], 6),
        "expected": [-1, -1],
    },
    {
        "description": "Empty array: [] target=0",
        "run": lambda: solution([], 0),
        "expected": [-1, -1],
    },
    {
        "description": "Single element found: [1] target=1",
        "run": lambda: solution([1], 1),
        "expected": [0, 0],
    },
    {
        "description": "All same: [2,2,2,2] target=2",
        "run": lambda: solution([2, 2, 2, 2], 2),
        "expected": [0, 3],
    },
]
