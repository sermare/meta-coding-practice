from problems.p462_lru_cache import solution

TEST_CASES = [
    {
        "description": "Basic LRU operations",
        "run": lambda: solution(["LRUCache","put","put","get","put","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]),
        "expected": [None,None,None,1,None,-1,None,-1,3,4],
    },
    {
        "description": "Single capacity",
        "run": lambda: solution(["LRUCache","put","put","get","get"], [[1],[1,1],[2,2],[1],[2]]),
        "expected": [None,None,None,-1,2],
    },
    {
        "description": "Update existing key",
        "run": lambda: solution(["LRUCache","put","put","get","put","get"], [[2],[1,1],[1,2],[1],[2,1],[2]]),
        "expected": [None,None,None,2,None,1],
    },
    {
        "description": "Get non-existent key",
        "run": lambda: solution(["LRUCache","get"], [[2],[1]]),
        "expected": [None,-1],
    },
]
