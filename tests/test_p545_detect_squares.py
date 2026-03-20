from problems.p545_detect_squares import solution

TEST_CASES = [
    {
        "description": "Basic count",
        "run": lambda: solution(["DetectSquares","add","add","add","count","count","add","count"], [[],[[3,10]],[[11,1]],[[3,1]],[[11,10]],[[14,8]],[[11,10]],[[11,10]]]),
        "expected": [None, None, None, None, 1, 0, None, 2],
    },
    {
        "description": "No square possible",
        "run": lambda: solution(["DetectSquares","add","count"], [[],[[1,1]],[[2,2]]]),
        "expected": [None, None, 0],
    },
    {
        "description": "Multiple squares",
        "run": lambda: solution(["DetectSquares","add","add","add","add","count"], [[],[[0,0]],[[0,1]],[[1,0]],[[1,1]],[[0,0]]]),
        "expected": [None, None, None, None, None, 1],
    },
    {
        "description": "Empty count",
        "run": lambda: solution(["DetectSquares","count"], [[],[[0,0]]]),
        "expected": [None, 0],
    },
]
