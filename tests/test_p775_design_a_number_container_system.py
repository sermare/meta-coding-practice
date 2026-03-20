from problems.p775_design_a_number_container_system import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(
            ["NumberContainers","find","change","change","change","change","find","change","find"],
            [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]
        ),
        "expected": [None,-1,None,None,None,None,1,None,2],
    },
    {
        "description": "Find non-existent number",
        "run": lambda: solution(
            ["NumberContainers","find"],
            [[],[99]]
        ),
        "expected": [None,-1],
    },
    {
        "description": "Replace at same index",
        "run": lambda: solution(
            ["NumberContainers","change","change","find","find"],
            [[],[1,5],[1,10],[5],[10]]
        ),
        "expected": [None,None,None,-1,1],
    },
    {
        "description": "Multiple indices same number",
        "run": lambda: solution(
            ["NumberContainers","change","change","find"],
            [[],[5,1],[3,1],[1]]
        ),
        "expected": [None,None,None,3],
    },
]
