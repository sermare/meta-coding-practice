from problems.p809_minimum_number_of_vertices_to_reach_all_nodes import solution

TEST_CASES = [
    {
        "description": "Two sources: n=6, edges=[[0,1],[0,2],[2,5],[3,4],[4,2]]",
        "run": lambda: sorted(solution(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])),
        "expected": [0,3],
    },
    {
        "description": "All isolated: n=3, edges=[]",
        "run": lambda: sorted(solution(3, [])),
        "expected": [0,1,2],
    },
    {
        "description": "Chain: n=3, edges=[[0,1],[1,2]]",
        "run": lambda: sorted(solution(3, [[0,1],[1,2]])),
        "expected": [0],
    },
    {
        "description": "Single node: n=1, edges=[]",
        "run": lambda: solution(1, []),
        "expected": [0],
    },
]
