from problems.p399_critical_connections_in_a_network import solution


TEST_CASES = [
    {
        "description": "One bridge: [1,3]",
        "run": lambda: sorted([sorted(e) for e in solution(4, [[0,1],[1,2],[2,0],[1,3]])]),
        "expected": [[1, 3]],
    },
    {
        "description": "Single edge is a bridge",
        "run": lambda: sorted([sorted(e) for e in solution(2, [[0, 1]])]),
        "expected": [[0, 1]],
    },
    {
        "description": "No bridges in a cycle",
        "run": lambda: solution(3, [[0, 1], [1, 2], [2, 0]]),
        "expected": [],
    },
    {
        "description": "Multiple bridges",
        "run": lambda: sorted([sorted(e) for e in solution(5, [[0,1],[1,2],[2,0],[2,3],[3,4]])]),
        "expected": [[2, 3], [3, 4]],
    },
]
