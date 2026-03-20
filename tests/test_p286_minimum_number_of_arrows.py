from problems.p286_minimum_number_of_arrows import solution

TEST_CASES = [
    {
        "description": "[[10,16],[2,8],[1,6],[7,12]] -> 2",
        "run": lambda: solution([[10, 16], [2, 8], [1, 6], [7, 12]]),
        "expected": 2,
    },
    {
        "description": "[[1,2],[3,4],[5,6],[7,8]] -> 4 (no overlap)",
        "run": lambda: solution([[1, 2], [3, 4], [5, 6], [7, 8]]),
        "expected": 4,
    },
    {
        "description": "[[1,2],[2,3],[3,4],[4,5]] -> 2",
        "run": lambda: solution([[1, 2], [2, 3], [3, 4], [4, 5]]),
        "expected": 2,
    },
    {
        "description": "[[1,10]] -> 1",
        "run": lambda: solution([[1, 10]]),
        "expected": 1,
    },
    {
        "description": "[[1,5],[2,6],[3,7]] -> 1",
        "run": lambda: solution([[1, 5], [2, 6], [3, 7]]),
        "expected": 1,
    },
]
