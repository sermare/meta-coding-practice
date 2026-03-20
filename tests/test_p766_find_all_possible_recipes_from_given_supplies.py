from problems.p766_find_all_possible_recipes_from_given_supplies import solution

TEST_CASES = [
    {
        "description": "Single recipe possible",
        "run": lambda: solution(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]),
        "expected": ["bread"],
    },
    {
        "description": "Chain dependency",
        "run": lambda: solution(["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]),
        "expected": ["bread","sandwich"],
    },
    {
        "description": "Missing ingredient",
        "run": lambda: solution(["bread"], [["yeast","flour"]], ["yeast"]),
        "expected": [],
    },
    {
        "description": "Multiple recipes, partial possible",
        "run": lambda: solution(["bread","cake"], [["yeast","flour"],["sugar","eggs"]], ["yeast","flour"]),
        "expected": ["bread"],
    },
]
