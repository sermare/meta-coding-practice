from problems.p834_check_if_grid_can_be_cut_into_sections import solution

TEST_CASES = [
    {
        "description": "Can cut: n=5",
        "run": lambda: solution(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]),
        "expected": True,
    },
    {
        "description": "Cannot cut: n=4, overlapping",
        "run": lambda: solution(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]),
        "expected": True,
    },
    {
        "description": "Single rectangle: n=3",
        "run": lambda: solution(3, [[0,0,3,3]]),
        "expected": False,
    },
    {
        "description": "Three separate: n=6",
        "run": lambda: solution(6, [[0,0,2,2],[2,2,4,4],[4,4,6,6]]),
        "expected": True,
    },
]
