from problems.p122_word_search_ii import solution

TEST_CASES = [
    {
        "description": "Standard board search",
        "run": lambda: sorted(solution(
            [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
            ["oath","pea","eat","rain"]
        )),
        "expected": ["eat", "oath"],
    },
    {
        "description": "No words found",
        "run": lambda: sorted(solution([["a","b"],["c","d"]], ["xyz"])),
        "expected": [],
    },
    {
        "description": "Single cell board",
        "run": lambda: sorted(solution([["a"]], ["a", "b"])),
        "expected": ["a"],
    },
    {
        "description": "All words found",
        "run": lambda: sorted(solution([["a","b"],["c","d"]], ["ab", "ac"])),
        "expected": ["ab", "ac"],
    },
]
