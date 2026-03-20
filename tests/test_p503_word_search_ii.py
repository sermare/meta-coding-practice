from problems.p503_word_search_ii import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: sorted(solution([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])),
        "expected": ["eat", "oath"],
    },
    {
        "description": "No matches",
        "run": lambda: solution([["a","b"],["c","d"]], ["xyz"]),
        "expected": [],
    },
    {
        "description": "Single cell",
        "run": lambda: solution([["a"]], ["a"]),
        "expected": ["a"],
    },
    {
        "description": "Single cell no match",
        "run": lambda: solution([["a"]], ["b"]),
        "expected": [],
    },
    {
        "description": "All found",
        "run": lambda: sorted(solution([["a","b"],["c","d"]], ["ab","cd","ac"])),
        "expected": ["ab", "ac", "cd"],
    },
]
