from problems.p635_number_of_connected_components_in_graph import solution

TEST_CASES = [
    {
        "description": "Two components: n=5, [[0,1],[1,2],[3,4]]",
        "run": lambda: solution(5, [[0, 1], [1, 2], [3, 4]]),
        "expected": 2,
    },
    {
        "description": "One component: n=5, [[0,1],[1,2],[2,3],[3,4]]",
        "run": lambda: solution(5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
        "expected": 1,
    },
    {
        "description": "All isolated: n=3, no edges",
        "run": lambda: solution(3, []),
        "expected": 3,
    },
    {
        "description": "Single node: n=1",
        "run": lambda: solution(1, []),
        "expected": 1,
    },
]
