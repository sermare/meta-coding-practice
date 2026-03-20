from problems.p229_number_of_atoms import solution

TEST_CASES = [
    {
        "description": "Simple: H2O",
        "run": lambda: solution("H2O"),
        "expected": "H2O",
    },
    {
        "description": "With parentheses: Mg(OH)2",
        "run": lambda: solution("Mg(OH)2"),
        "expected": "H2MgO2",
    },
    {
        "description": "Nested: K4(ON(SO3)2)2",
        "run": lambda: solution("K4(ON(SO3)2)2"),
        "expected": "K4N2O14S4",
    },
    {
        "description": "Single element: O",
        "run": lambda: solution("O"),
        "expected": "O",
    },
]
