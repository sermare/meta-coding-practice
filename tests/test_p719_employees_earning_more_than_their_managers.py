from problems.p719_employees_earning_more_than_their_managers import solution

TEST_CASES = [
    {
        "description": "One employee earns more than manager",
        "run": lambda: solution([
            {"id": 1, "name": "Joe", "salary": 70000, "managerId": 3},
            {"id": 2, "name": "Henry", "salary": 80000, "managerId": 4},
            {"id": 3, "name": "Sam", "salary": 60000, "managerId": None},
            {"id": 4, "name": "Max", "salary": 90000, "managerId": None},
        ]),
        "expected": ["Joe"],
    },
    {
        "description": "No one earns more than manager",
        "run": lambda: solution([
            {"id": 1, "name": "A", "salary": 50000, "managerId": 2},
            {"id": 2, "name": "B", "salary": 80000, "managerId": None},
        ]),
        "expected": [],
    },
    {
        "description": "Multiple employees earn more",
        "run": lambda: solution([
            {"id": 1, "name": "A", "salary": 90000, "managerId": 3},
            {"id": 2, "name": "B", "salary": 80000, "managerId": 3},
            {"id": 3, "name": "C", "salary": 50000, "managerId": None},
        ]),
        "expected": ["A", "B"],
    },
    {
        "description": "Empty list",
        "run": lambda: solution([]),
        "expected": [],
    },
]
