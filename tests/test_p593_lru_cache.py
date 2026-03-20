from problems.p593_lru_cache import solution

TEST_CASES = [
    {
        "description": "Standard LRU eviction",
        "run": lambda: solution(
            2,
            ["put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        ),
        "expected": [None, None, 1, None, -1, None, -1, 3, 4],
    },
    {
        "description": "Get refreshes usage",
        "run": lambda: solution(
            2,
            ["put", "put", "get", "put", "get"],
            [[1, 1], [2, 2], [1], [3, 3], [2]]
        ),
        "expected": [None, None, 1, None, -1],
    },
    {
        "description": "Capacity 1",
        "run": lambda: solution(
            1,
            ["put", "put", "get"],
            [[1, 1], [2, 2], [1]]
        ),
        "expected": [None, None, -1],
    },
    {
        "description": "Update existing key",
        "run": lambda: solution(
            2,
            ["put", "put", "get"],
            [[1, 1], [1, 10], [1]]
        ),
        "expected": [None, None, 10],
    },
]
