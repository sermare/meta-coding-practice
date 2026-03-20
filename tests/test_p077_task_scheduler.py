from problems.p077_task_scheduler import solution

TEST_CASES = [
    {
        "description": "Standard: [A,A,A,B,B,B] n=2",
        "run": lambda: solution(["A", "A", "A", "B", "B", "B"], 2),
        "expected": 8,
    },
    {
        "description": "No idle needed: [A,C,A,B,D,B] n=1",
        "run": lambda: solution(["A", "C", "A", "B", "D", "B"], 1),
        "expected": 6,
    },
    {
        "description": "Large gap: [A,A,A,B,B,B] n=3",
        "run": lambda: solution(["A", "A", "A", "B", "B", "B"], 3),
        "expected": 10,
    },
    {
        "description": "Single task: [A] n=2",
        "run": lambda: solution(["A"], 2),
        "expected": 1,
    },
    {
        "description": "No cooldown: [A,A,A] n=0",
        "run": lambda: solution(["A", "A", "A"], 0),
        "expected": 3,
    },
]
