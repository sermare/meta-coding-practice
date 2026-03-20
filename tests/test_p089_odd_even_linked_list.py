from problems.p089_odd_even_linked_list import solution, build_list, list_to_array

TEST_CASES = [
    {
        "description": "Odd length: [1,2,3,4,5]",
        "run": lambda: list_to_array(solution(build_list([1, 2, 3, 4, 5]))),
        "expected": [1, 3, 5, 2, 4],
    },
    {
        "description": "Even length: [2,1,3,5,6,4,7]",
        "run": lambda: list_to_array(solution(build_list([2, 1, 3, 5, 6, 4, 7]))),
        "expected": [2, 3, 6, 7, 1, 5, 4],
    },
    {
        "description": "Empty list",
        "run": lambda: list_to_array(solution(build_list([]))),
        "expected": [],
    },
    {
        "description": "Single element: [1]",
        "run": lambda: list_to_array(solution(build_list([1]))),
        "expected": [1],
    },
    {
        "description": "Two elements: [1,2]",
        "run": lambda: list_to_array(solution(build_list([1, 2]))),
        "expected": [1, 2],
    },
]
