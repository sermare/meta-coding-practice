from problems.p125_analyze_user_website_visit_pattern import solution

TEST_CASES = [
    {
        "description": "Standard example",
        "run": lambda: solution(
            ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
            [1,2,3,4,5,6,7,8,9,10],
            ["home","about","career","home","cart","maps","home","home","about","career"]
        ),
        "expected": ["home", "about", "career"],
    },
    {
        "description": "All same user",
        "run": lambda: solution(
            ["u","u","u","u"],
            [1,2,3,4],
            ["a","b","a","c"]
        ),
        "expected": ["a", "a", "c"],
    },
    {
        "description": "Tie broken lexicographically",
        "run": lambda: solution(
            ["a","a","a","b","b","b"],
            [1,2,3,4,5,6],
            ["x","y","z","x","y","z"]
        ),
        "expected": ["x", "y", "z"],
    },
    {
        "description": "Minimal input",
        "run": lambda: solution(
            ["u","u","u"],
            [1,2,3],
            ["a","b","c"]
        ),
        "expected": ["a", "b", "c"],
    },
]
