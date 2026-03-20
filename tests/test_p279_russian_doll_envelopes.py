from problems.p279_russian_doll_envelopes import solution

TEST_CASES = [
    {
        "description": "[[5,4],[6,4],[6,7],[2,3]] -> 3",
        "run": lambda: solution([[5, 4], [6, 4], [6, 7], [2, 3]]),
        "expected": 3,
    },
    {
        "description": "[[1,1],[1,1],[1,1]] -> 1",
        "run": lambda: solution([[1, 1], [1, 1], [1, 1]]),
        "expected": 1,
    },
    {
        "description": "[[1,1]] -> 1",
        "run": lambda: solution([[1, 1]]),
        "expected": 1,
    },
    {
        "description": "[[1,2],[2,3],[3,4],[4,5]] -> 4",
        "run": lambda: solution([[1, 2], [2, 3], [3, 4], [4, 5]]),
        "expected": 4,
    },
    {
        "description": "[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]] -> 5",
        "run": lambda: solution([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]),
        "expected": 5,
    },
]
