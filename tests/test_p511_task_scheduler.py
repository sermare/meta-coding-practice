from problems.p511_task_scheduler import solution

TEST_CASES = [
    {
        "description": "Basic case n=2",
        "run": lambda: solution(["A","A","A","B","B","B"], 2),
        "expected": 8,
    },
    {
        "description": "No cooldown",
        "run": lambda: solution(["A","A","A","B","B","B"], 0),
        "expected": 6,
    },
    {
        "description": "Single task type",
        "run": lambda: solution(["A","A","A"], 2),
        "expected": 7,
    },
    {
        "description": "Many types no idle",
        "run": lambda: solution(["A","B","C","D"], 2),
        "expected": 4,
    },
    {
        "description": "n=1",
        "run": lambda: solution(["A","A","A","B","B","B"], 1),
        "expected": 6,
    },
]
