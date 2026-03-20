from problems.p398_satisfiability_of_equality_equations import solution


TEST_CASES = [
    {
        "description": "Contradiction: a==b and b!=a",
        "run": lambda: solution(["a==b", "b!=a"]),
        "expected": False,
    },
    {
        "description": "Consistent equalities",
        "run": lambda: solution(["b==a", "a==b"]),
        "expected": True,
    },
    {
        "description": "Transitive equalities",
        "run": lambda: solution(["a==b", "b==c", "a==c"]),
        "expected": True,
    },
    {
        "description": "Cycle contradiction",
        "run": lambda: solution(["a==b", "b!=c", "c==a"]),
        "expected": False,
    },
    {
        "description": "Independent inequalities",
        "run": lambda: solution(["a!=b", "c!=d"]),
        "expected": True,
    },
]
