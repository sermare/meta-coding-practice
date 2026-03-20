from problems.p123_design_hit_counter import solution

TEST_CASES = [
    {
        "description": "Standard hit counter usage",
        "run": lambda: solution(
            ["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"],
            [[],[1],[2],[3],[4],[300],[300],[301]]
        ),
        "expected": [None, None, None, None, 3, None, 4, 3],
    },
    {
        "description": "All hits expired",
        "run": lambda: solution(
            ["HitCounter","hit","getHits"],
            [[],[1],[301]]
        ),
        "expected": [None, None, 0],
    },
    {
        "description": "Hits at same timestamp",
        "run": lambda: solution(
            ["HitCounter","hit","hit","hit","getHits"],
            [[],[1],[1],[1],[1]]
        ),
        "expected": [None, None, None, None, 3],
    },
    {
        "description": "No hits, get returns 0",
        "run": lambda: solution(
            ["HitCounter","getHits"],
            [[],[100]]
        ),
        "expected": [None, 0],
    },
]
