from problems.p650_design_search_autocomplete_system import solution

TEST_CASES = [
    {
        "description": "Basic autocomplete",
        "run": lambda: solution(
            ["i love you", "island", "iroman", "i love leetcode"],
            [5, 3, 2, 2],
            ["i", " ", "a", "#"]
        ),
        "expected": [
            ["i love you", "island", "i love leetcode"],
            ["i love you", "i love leetcode"],
            [],
            []
        ],
    },
    {
        "description": "Empty input starts",
        "run": lambda: solution(
            ["hello"],
            [1],
            ["#"]
        ),
        "expected": [[]],
    },
    {
        "description": "Single sentence match",
        "run": lambda: solution(
            ["abc", "abd"],
            [3, 2],
            ["a", "b", "c", "#"]
        ),
        "expected": [["abc", "abd"], ["abc", "abd"], ["abc"], []],
    },
    {
        "description": "No matches",
        "run": lambda: solution(
            ["hello"],
            [1],
            ["x", "#"]
        ),
        "expected": [[], []],
    },
]
