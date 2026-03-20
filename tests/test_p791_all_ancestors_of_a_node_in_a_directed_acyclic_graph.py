from problems.p791_all_ancestors_of_a_node_in_a_directed_acyclic_graph import solution

TEST_CASES = [
    {
        "description": "Basic DAG: n=8",
        "run": lambda: solution(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]),
        "expected": [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]],
    },
    {
        "description": "No edges: n=3",
        "run": lambda: solution(3, []),
        "expected": [[],[],[]],
    },
    {
        "description": "Linear chain: n=3, [[0,1],[1,2]]",
        "run": lambda: solution(3, [[0,1],[1,2]]),
        "expected": [[],[0],[0,1]],
    },
    {
        "description": "Single edge: n=2, [[0,1]]",
        "run": lambda: solution(2, [[0,1]]),
        "expected": [[],[0]],
    },
]
