from problems.p751_design_browser_history import solution

TEST_CASES = [
    {
        "description": "Basic navigation with back and forward",
        "run": lambda: solution(
            ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"],
            [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
        ),
        "expected": [None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"],
    },
    {
        "description": "Back more steps than history",
        "run": lambda: solution(
            ["BrowserHistory","visit","back"],
            [["home.com"],["page1.com"],[5]]
        ),
        "expected": [None,None,"home.com"],
    },
    {
        "description": "Forward with no forward history",
        "run": lambda: solution(
            ["BrowserHistory","forward"],
            [["home.com"],[3]]
        ),
        "expected": [None,"home.com"],
    },
    {
        "description": "Visit clears forward history",
        "run": lambda: solution(
            ["BrowserHistory","visit","visit","back","visit","forward"],
            [["a.com"],["b.com"],["c.com"],[1],["d.com"],[1]]
        ),
        "expected": [None,None,None,"b.com",None,"d.com"],
    },
]
