from problems.p397_regions_cut_by_slashes import solution


TEST_CASES = [
    {
        "description": "Two regions from /",
        "run": lambda: solution([" /", "/ "]),
        "expected": 2,
    },
    {
        "description": "One region",
        "run": lambda: solution([" /", "  "]),
        "expected": 1,
    },
    {
        "description": "Four regions from X pattern",
        "run": lambda: solution(["/\\", "\\/"]),
        "expected": 4,
    },
    {
        "description": "Single empty cell",
        "run": lambda: solution([" "]),
        "expected": 1,
    },
]
