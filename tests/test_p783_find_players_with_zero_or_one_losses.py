from problems.p783_find_players_with_zero_or_one_losses import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]),
        "expected": [[1,2,10],[4,5,7,8]],
    },
    {
        "description": "Single match: [[1,2]]",
        "run": lambda: solution([[1,2]]),
        "expected": [[1],[2]],
    },
    {
        "description": "Two losses: [[2,3],[1,3],[5,4],[6,4]]",
        "run": lambda: solution([[2,3],[1,3],[5,4],[6,4]]),
        "expected": [[1,2,5,6],[]],
    },
    {
        "description": "Chain: [[1,2],[2,3],[3,4]]",
        "run": lambda: solution([[1,2],[2,3],[3,4]]),
        "expected": [[1],[2,3,4]],
    },
]
