from problems.p467_min_stack import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]),
        "expected": [None,None,None,None,-3,None,0,-2],
    },
    {
        "description": "Single element",
        "run": lambda: solution(["MinStack","push","getMin","top"], [[],[5],[],[]]),
        "expected": [None,None,5,5],
    },
    {
        "description": "Push and pop all",
        "run": lambda: solution(["MinStack","push","push","pop","getMin"], [[],[1],[2],[],[]]),
        "expected": [None,None,None,None,1],
    },
    {
        "description": "Decreasing elements",
        "run": lambda: solution(["MinStack","push","push","push","getMin"], [[],[3],[2],[1],[]]),
        "expected": [None,None,None,None,1],
    },
]
