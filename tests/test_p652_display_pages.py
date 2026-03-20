from problems.p652_display_pages import solution

TEST_CASES = [
    {
        "description": "Basic pagination with host dedup",
        "run": lambda: solution([
            "1,28,300.1,SF",
            "4,5,209.1,SF",
            "1,7,208.0,SF",
            "3,8,207.0,Oak",
        ], 2),
        "expected": [
            "1,28,300.1,SF",
            "4,5,209.1,SF",
            "",
            "1,7,208.0,SF",
            "3,8,207.0,Oak",
        ],
    },
    {
        "description": "Single page fits all",
        "run": lambda: solution(["1,1,100,A", "2,2,90,B"], 5),
        "expected": ["1,1,100,A", "2,2,90,B"],
    },
    {
        "description": "All same host",
        "run": lambda: solution(["1,1,100,A", "1,2,90,A", "1,3,80,A"], 2),
        "expected": ["1,1,100,A", "1,2,90,A", "", "1,3,80,A"],
    },
    {
        "description": "Empty input",
        "run": lambda: solution([], 3),
        "expected": [],
    },
]
