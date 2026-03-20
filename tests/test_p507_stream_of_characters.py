from problems.p507_stream_of_characters import solution

TEST_CASES = [
    {
        "description": "Basic stream",
        "run": lambda: solution(["StreamChecker","query","query","query","query","query","query"], [[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"]]),
        "expected": [None, False, False, False, True, False, True],
    },
    {
        "description": "Single char word",
        "run": lambda: solution(["StreamChecker","query","query"], [[["a"]],["a"],["b"]]),
        "expected": [None, True, False],
    },
    {
        "description": "Multi match",
        "run": lambda: solution(["StreamChecker","query","query","query"], [[["ab","b"]],["a"],["b"],["b"]]),
        "expected": [None, False, True, True],
    },
    {
        "description": "No match ever",
        "run": lambda: solution(["StreamChecker","query","query"], [[["xyz"]],["a"],["b"]]),
        "expected": [None, False, False],
    },
]
