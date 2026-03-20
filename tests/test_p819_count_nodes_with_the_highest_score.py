from problems.p819_count_nodes_with_the_highest_score import solution

TEST_CASES = [
    {
        "description": "5 nodes: parents=[-1,2,0,2,0]",
        "run": lambda: solution([-1, 2, 0, 2, 0]),
        "expected": 3,
    },
    {
        "description": "2 nodes: parents=[-1,0]",
        "run": lambda: solution([-1, 0]),
        "expected": 2,
    },
    {
        "description": "Chain: parents=[-1,0,1]",
        "run": lambda: solution([-1, 0, 1]),
        "expected": 2,
    },
    {
        "description": "Star: parents=[-1,0,0,0]",
        "run": lambda: solution([-1, 0, 0, 0]),
        "expected": 3,
    },
]
