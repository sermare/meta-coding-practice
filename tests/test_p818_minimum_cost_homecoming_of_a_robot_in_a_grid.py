from problems.p818_minimum_cost_homecoming_of_a_robot_in_a_grid import solution

TEST_CASES = [
    {
        "description": "Basic: start=[1,0] home=[2,3]",
        "run": lambda: solution([1,0], [2,3], [5,4,3], [8,2,6,7]),
        "expected": 18,
    },
    {
        "description": "Same position: start=[0,0] home=[0,0]",
        "run": lambda: solution([0,0], [0,0], [5], [5]),
        "expected": 0,
    },
    {
        "description": "Move right only: start=[0,0] home=[0,2]",
        "run": lambda: solution([0,0], [0,2], [1], [1,2,3]),
        "expected": 5,
    },
    {
        "description": "Move down only: start=[0,0] home=[2,0]",
        "run": lambda: solution([0,0], [2,0], [1,2,3], [1]),
        "expected": 5,
    },
]
