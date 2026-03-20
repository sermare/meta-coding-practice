from problems.p056_remove_nth_node_from_end_of_list import solution, build_list, list_to_array

TEST_CASES = [
    {
        "description": "Remove 2nd from end: [1,2,3,4,5] n=2",
        "run": lambda: list_to_array(solution(build_list([1, 2, 3, 4, 5]), 2)),
        "expected": [1, 2, 3, 5],
    },
    {
        "description": "Single node: [1] n=1",
        "run": lambda: list_to_array(solution(build_list([1]), 1)),
        "expected": [],
    },
    {
        "description": "Remove last: [1,2] n=1",
        "run": lambda: list_to_array(solution(build_list([1, 2]), 1)),
        "expected": [1],
    },
    {
        "description": "Remove first: [1,2] n=2",
        "run": lambda: list_to_array(solution(build_list([1, 2]), 2)),
        "expected": [2],
    },
]
