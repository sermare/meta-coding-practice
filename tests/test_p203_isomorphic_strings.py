from problems.p203_isomorphic_strings import solution

TEST_CASES = [
    {
        "description": "Isomorphic: egg -> add",
        "run": lambda: solution("egg", "add"),
        "expected": True,
    },
    {
        "description": "Not isomorphic: foo -> bar",
        "run": lambda: solution("foo", "bar"),
        "expected": False,
    },
    {
        "description": "Isomorphic: paper -> title",
        "run": lambda: solution("paper", "title"),
        "expected": True,
    },
    {
        "description": "Single char: a -> b",
        "run": lambda: solution("a", "b"),
        "expected": True,
    },
    {
        "description": "Not isomorphic: badc -> baba",
        "run": lambda: solution("badc", "baba"),
        "expected": False,
    },
]
