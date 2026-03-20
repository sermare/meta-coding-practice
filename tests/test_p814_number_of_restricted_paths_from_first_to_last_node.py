from problems.p814_number_of_restricted_paths_from_first_to_last_node import solution

TEST_CASES = [
    {
        "description": "5-node graph: 3 restricted paths",
        "run": lambda: solution(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]),
        "expected": 3,
    },
    {
        "description": "Simple: n=2, one edge",
        "run": lambda: solution(2, [[1,2,1]]),
        "expected": 1,
    },
    {
        "description": "7-node graph",
        "run": lambda: solution(7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]),
        "expected": 1,
    },
    {
        "description": "Triangle: n=3",
        "run": lambda: solution(3, [[1,2,1],[2,3,1],[1,3,3]]),
        "expected": 2,
    },
]
