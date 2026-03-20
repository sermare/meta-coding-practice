from problems.p546_rotate_image import solution

TEST_CASES = [
    {
        "description": "3x3 matrix",
        "run": lambda: solution([[1,2,3],[4,5,6],[7,8,9]]),
        "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
    },
    {
        "description": "2x2 matrix",
        "run": lambda: solution([[1,2],[3,4]]),
        "expected": [[3, 1], [4, 2]],
    },
    {
        "description": "1x1 matrix",
        "run": lambda: solution([[1]]),
        "expected": [[1]],
    },
    {
        "description": "4x4 matrix",
        "run": lambda: solution([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]),
        "expected": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    },
]
