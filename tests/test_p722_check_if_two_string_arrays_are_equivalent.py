from problems.p722_check_if_two_string_arrays_are_equivalent import solution

TEST_CASES = [
    {
        "description": "Equivalent: ['ab','c'] and ['a','bc']",
        "run": lambda: solution(["ab", "c"], ["a", "bc"]),
        "expected": True,
    },
    {
        "description": "Not equivalent: ['a','cb'] and ['ab','c']",
        "run": lambda: solution(["a", "cb"], ["ab", "c"]),
        "expected": False,
    },
    {
        "description": "Single strings: ['abc'] and ['abc']",
        "run": lambda: solution(["abc"], ["abc"]),
        "expected": True,
    },
    {
        "description": "Many parts: ['a','b','c'] and ['abc']",
        "run": lambda: solution(["a", "b", "c"], ["abc"]),
        "expected": True,
    },
]
