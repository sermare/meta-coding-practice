from problems.p055_longest_common_prefix import solution

TEST_CASES = [
    {
        "description": "Common prefix fl: flower, flow, flight",
        "run": lambda: solution(["flower", "flow", "flight"]),
        "expected": "fl",
    },
    {
        "description": "No common prefix: dog, racecar, car",
        "run": lambda: solution(["dog", "racecar", "car"]),
        "expected": "",
    },
    {
        "description": "Single string: hello",
        "run": lambda: solution(["hello"]),
        "expected": "hello",
    },
    {
        "description": "All same: abc, abc, abc",
        "run": lambda: solution(["abc", "abc", "abc"]),
        "expected": "abc",
    },
    {
        "description": "Empty string in list",
        "run": lambda: solution(["", "b"]),
        "expected": "",
    },
]
