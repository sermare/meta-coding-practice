from problems.p837_longest_common_prefix import solution

TEST_CASES = [
    {
        "description": "Common prefix fl: [flower,flow,flight]",
        "run": lambda: solution(["flower", "flow", "flight"]),
        "expected": "fl",
    },
    {
        "description": "No common prefix: [dog,racecar,car]",
        "run": lambda: solution(["dog", "racecar", "car"]),
        "expected": "",
    },
    {
        "description": "All same: [abc,abc,abc]",
        "run": lambda: solution(["abc", "abc", "abc"]),
        "expected": "abc",
    },
    {
        "description": "Single string: [hello]",
        "run": lambda: solution(["hello"]),
        "expected": "hello",
    },
    {
        "description": "Empty string in list: [,'abc']",
        "run": lambda: solution(["", "abc"]),
        "expected": "",
    },
]
