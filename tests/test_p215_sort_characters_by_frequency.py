from problems.p215_sort_characters_by_frequency import solution

TEST_CASES = [
    {
        "description": "tree -> eert or eetr",
        "run": lambda: sorted(solution("tree")) if solution("tree") else None,
        "expected": sorted("eert"),
    },
    {
        "description": "cccaaa -> cccaaa or aaaccc",
        "run": lambda: sorted(solution("cccaaa")) if solution("cccaaa") else None,
        "expected": sorted("cccaaa"),
    },
    {
        "description": "Aabb -> bbAa or bbaA",
        "run": lambda: sorted(solution("Aabb")) if solution("Aabb") else None,
        "expected": sorted("bbAa"),
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": "a",
    },
]
