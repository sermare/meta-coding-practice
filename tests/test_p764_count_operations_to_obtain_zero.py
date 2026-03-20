from problems.p764_count_operations_to_obtain_zero import solution

TEST_CASES = [
    {
        "description": "Basic: num1=2, num2=3",
        "run": lambda: solution(2, 3),
        "expected": 3,
    },
    {
        "description": "Equal: num1=10, num2=10",
        "run": lambda: solution(10, 10),
        "expected": 1,
    },
    {
        "description": "One is zero: num1=0, num2=5",
        "run": lambda: solution(0, 5),
        "expected": 0,
    },
    {
        "description": "Larger case: num1=5, num2=2",
        "run": lambda: solution(5, 2),
        "expected": 4,
    },
]
