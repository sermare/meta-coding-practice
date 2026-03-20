from problems.p199_implement_queue_using_stacks import solution

TEST_CASES = [
    {
        "description": "Basic queue operations",
        "run": lambda: solution(["push","push","peek","pop","empty"], [[1],[2],[],[],[]]),
        "expected": [None, None, 1, 1, False],
    },
    {
        "description": "Empty after all pops",
        "run": lambda: solution(["push","pop","empty"], [[1],[],[]]),
        "expected": [None, 1, True],
    },
    {
        "description": "FIFO order",
        "run": lambda: solution(["push","push","push","pop","pop","pop"], [[1],[2],[3],[],[],[]]),
        "expected": [None, None, None, 1, 2, 3],
    },
    {
        "description": "Peek does not remove",
        "run": lambda: solution(["push","peek","peek","pop"], [[5],[],[],[]]),
        "expected": [None, 5, 5, 5],
    },
]
