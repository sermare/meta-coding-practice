from problems.p463_lfu_cache import solution

TEST_CASES = [
    {
        "description": "Basic LFU operations",
        "run": lambda: solution(["LFUCache","put","put","get","put","get","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]),
        "expected": [None,None,None,1,None,-1,3,None,1,3,4],
    },
    {
        "description": "Single capacity",
        "run": lambda: solution(["LFUCache","put","get","put","get","get"], [[1],[1,1],[1],[2,2],[1],[2]]),
        "expected": [None,None,1,None,-1,2],
    },
    {
        "description": "Update existing key",
        "run": lambda: solution(["LFUCache","put","put","put","get"], [[2],[1,1],[2,2],[1,3],[1]]),
        "expected": [None,None,None,None,3],
    },
    {
        "description": "Get non-existent key",
        "run": lambda: solution(["LFUCache","get"], [[2],[1]]),
        "expected": [None,-1],
    },
]
