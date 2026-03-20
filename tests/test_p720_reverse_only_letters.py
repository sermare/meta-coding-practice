from problems.p720_reverse_only_letters import solution

TEST_CASES = [
    {
        "description": "Basic case: 'ab-cd'",
        "run": lambda: solution("ab-cd"),
        "expected": "dc-ba",
    },
    {
        "description": "Complex case: 'a-bC-dEf-ghIj'",
        "run": lambda: solution("a-bC-dEf-ghIj"),
        "expected": "j-Ih-gfE-dCba",
    },
    {
        "description": "No letters: '---'",
        "run": lambda: solution("---"),
        "expected": "---",
    },
    {
        "description": "No specials: 'abc'",
        "run": lambda: solution("abc"),
        "expected": "cba",
    },
    {
        "description": "Single letter: 'a'",
        "run": lambda: solution("a"),
        "expected": "a",
    },
]
