from problems.p826_maximum_number_of_groups_entering_a_competition import solution

TEST_CASES = [
    {
        "description": "6 students: [10,6,12,7,3,5]",
        "run": lambda: solution([10, 6, 12, 7, 3, 5]),
        "expected": 3,
    },
    {
        "description": "Single student: [8]",
        "run": lambda: solution([8]),
        "expected": 1,
    },
    {
        "description": "3 students: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": 2,
    },
    {
        "description": "10 students",
        "run": lambda: solution([1,2,3,4,5,6,7,8,9,10]),
        "expected": 4,
    },
]
