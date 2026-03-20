from problems.p778_count_unreachable_pairs_of_nodes_in_an_undirected_graph import solution

TEST_CASES = [
    {
        "description": "Fully connected: n=3, edges=[[0,1],[0,2],[1,2]]",
        "run": lambda: solution(3, [[0,1],[0,2],[1,2]]),
        "expected": 0,
    },
    {
        "description": "Two components: n=7, edges=[[0,2],[0,5],[2,4],[1,6],[5,4]]",
        "run": lambda: solution(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]),
        "expected": 14,
    },
    {
        "description": "No edges: n=3, edges=[]",
        "run": lambda: solution(3, []),
        "expected": 3,
    },
    {
        "description": "Single node: n=1, edges=[]",
        "run": lambda: solution(1, []),
        "expected": 0,
    },
]
