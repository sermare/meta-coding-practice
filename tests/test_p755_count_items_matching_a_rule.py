from problems.p755_count_items_matching_a_rule import solution

TEST_CASES = [
    {
        "description": "Match by color",
        "run": lambda: solution([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"),
        "expected": 1,
    },
    {
        "description": "Match by type",
        "run": lambda: solution([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "type", "phone"),
        "expected": 2,
    },
    {
        "description": "Match by name",
        "run": lambda: solution([["phone","blue","pixel"],["computer","silver","pixel"]], "name", "pixel"),
        "expected": 2,
    },
    {
        "description": "No matches",
        "run": lambda: solution([["phone","blue","pixel"]], "type", "laptop"),
        "expected": 0,
    },
]
