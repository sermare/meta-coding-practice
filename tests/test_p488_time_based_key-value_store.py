from problems.p488_time_based_key-value_store import solution

TEST_CASES = [
    {
        "description": "Basic set and get",
        "run": lambda: solution(["TimeMap","set","get","get","set","get"], [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4]]),
        "expected": [None,None,"bar","bar",None,"bar2"],
    },
    {
        "description": "Get before any set",
        "run": lambda: solution(["TimeMap","get"], [[],["foo",1]]),
        "expected": [None,""],
    },
    {
        "description": "Multiple keys",
        "run": lambda: solution(["TimeMap","set","set","get","get"], [[],["a","1",1],["b","2",2],["a",1],["b",2]]),
        "expected": [None,None,None,"1","2"],
    },
    {
        "description": "Get at exact timestamp",
        "run": lambda: solution(["TimeMap","set","set","get"], [[],["k","v1",1],["k","v2",2],["k",2]]),
        "expected": [None,None,None,"v2"],
    },
]
