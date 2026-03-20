from problems.p083_shortest_path_to_get_all_keys import solution

TEST_CASES = [
    {
        "description": "Two keys: @.a.. / ###.# / b.A.B",
        "run": lambda: solution(["@.a..", "###.#", "b.A.B"]),
        "expected": 8,
    },
    {
        "description": "Two keys adjacent: @..aA / ..B#. / ....b",
        "run": lambda: solution(["@..aA", "..B#.", "....b"]),
        "expected": 6,
    },
    {
        "description": "Impossible: @Aa",
        "run": lambda: solution(["@Aa"]),
        "expected": -1,
    },
    {
        "description": "Key right next to start: @a",
        "run": lambda: solution(["@a"]),
        "expected": 1,
    },
]
