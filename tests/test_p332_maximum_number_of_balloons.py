from problems.p332_maximum_number_of_balloons import solution

TEST_CASES = [
    {
        "description": "One balloon: nlaebolko",
        "run": lambda: solution("nlaebolko"),
        "expected": 1,
    },
    {
        "description": "Two balloons: loonbalxballpoon",
        "run": lambda: solution("loonbalxballpoon"),
        "expected": 2,
    },
    {
        "description": "No balloon possible: leetcode",
        "run": lambda: solution("leetcode"),
        "expected": 0,
    },
    {
        "description": "Exact balloon",
        "run": lambda: solution("balloon"),
        "expected": 1,
    },
]
