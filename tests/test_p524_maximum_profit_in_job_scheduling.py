from problems.p524_maximum_profit_in_job_scheduling import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([1,2,3,3], [3,4,5,6], [50,10,40,70]),
        "expected": 120,
    },
    {
        "description": "All overlap, pick best",
        "run": lambda: solution([1,1,1], [2,3,4], [5,6,4]),
        "expected": 6,
    },
    {
        "description": "No overlap",
        "run": lambda: solution([1,3,5], [2,4,6], [10,20,30]),
        "expected": 60,
    },
    {
        "description": "Single job",
        "run": lambda: solution([1], [2], [50]),
        "expected": 50,
    },
    {
        "description": "Chain of jobs",
        "run": lambda: solution([1,2,3,4], [2,3,4,5], [10,20,30,40]),
        "expected": 100,
    },
]
