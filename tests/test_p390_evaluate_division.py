from problems.p390_evaluate_division import solution


TEST_CASES = [
    {
        "description": "Standard evaluation",
        "run": lambda: solution([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
        "expected": [6.0, 0.5, -1.0, 1.0, -1.0],
    },
    {
        "description": "Chain evaluation",
        "run": lambda: solution([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),
        "expected": [3.75, 0.4, 5.0, 0.2],
    },
    {
        "description": "Single equation",
        "run": lambda: solution([["a","b"]], [2.0], [["a","b"],["b","a"]]),
        "expected": [2.0, 0.5],
    },
    {
        "description": "Unknown variables",
        "run": lambda: solution([["a","b"]], [2.0], [["x","y"]]),
        "expected": [-1.0],
    },
]
