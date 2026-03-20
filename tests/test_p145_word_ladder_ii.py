from problems.p145_word_ladder_ii import solution

TEST_CASES = [
    {
        "description": "Two shortest paths",
        "run": lambda: sorted(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"])),
        "expected": sorted([["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]),
    },
    {
        "description": "No path exists",
        "run": lambda: solution("hit", "cog", ["hot","dot","dog","lot","log"]),
        "expected": [],
    },
    {
        "description": "Direct one-step transform",
        "run": lambda: solution("hot", "dot", ["dot"]),
        "expected": [["hot", "dot"]],
    },
    {
        "description": "Single path available",
        "run": lambda: solution("a", "c", ["b", "c"]),
        "expected": [["a", "c"]],
    },
]
