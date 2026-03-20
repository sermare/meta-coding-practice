from problems.p017_lru_cache import solution


def _run_lru_test():
    cache = solution(2)
    cache.put(1, 1)
    cache.put(2, 2)
    r1 = cache.get(1)       # returns 1
    cache.put(3, 3)          # evicts key 2
    r2 = cache.get(2)       # returns -1 (not found)
    cache.put(4, 4)          # evicts key 1
    r3 = cache.get(1)       # returns -1 (not found)
    r4 = cache.get(3)       # returns 3
    r5 = cache.get(4)       # returns 4
    return [r1, r2, r3, r4, r5]


TEST_CASES = [
    {
        "description": "LRU Cache: capacity=2, sequence of put/get operations",
        "run": _run_lru_test,
        "expected": [1, -1, -1, 3, 4],
    },
]
