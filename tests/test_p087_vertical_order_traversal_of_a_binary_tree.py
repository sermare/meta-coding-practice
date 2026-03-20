from problems.p087_vertical_order_traversal_of_a_binary_tree import solution, build_tree

TEST_CASES = [
    {
        "description": "Standard: [3,9,20,null,null,15,7]",
        "run": lambda: solution(build_tree([3, 9, 20, None, None, 15, 7])),
        "expected": [[9], [3, 15], [20], [7]],
    },
    {
        "description": "Full tree: [1,2,3,4,5,6,7]",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 5, 6, 7])),
        "expected": [[4], [2], [1, 5, 6], [3], [7]],
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution(build_tree([1])),
        "expected": [[1]],
    },
    {
        "description": "Same position sort: [1,2,3,4,6,5,7]",
        "run": lambda: solution(build_tree([1, 2, 3, 4, 6, 5, 7])),
        "expected": [[4], [2], [1, 5, 6], [3], [7]],
    },
]
