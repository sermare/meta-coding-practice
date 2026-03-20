from problems.p796_count_prefixes_of_a_given_string import solution

TEST_CASES = [
    {
        "description": "Basic: words=['a','b','c','ab','bc','abc'], s='abc'",
        "run": lambda: solution(["a","b","c","ab","bc","abc"], "abc"),
        "expected": 3,
    },
    {
        "description": "No prefixes: words=['x','y'], s='abc'",
        "run": lambda: solution(["x","y"], "abc"),
        "expected": 0,
    },
    {
        "description": "All prefixes: words=['a','ab','abc'], s='abcd'",
        "run": lambda: solution(["a","ab","abc"], "abcd"),
        "expected": 3,
    },
    {
        "description": "Empty words: words=[], s='abc'",
        "run": lambda: solution([], "abc"),
        "expected": 0,
    },
]
