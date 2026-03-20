from problems.p560_design_underground_system import solution

TEST_CASES = [
    {
        "description": "Single trip average",
        "run": lambda: solution(
            ["checkIn", "checkOut", "getAverageTime"],
            [[45, "Leyton", 3], [45, "Waterloo", 15], ["Leyton", "Waterloo"]]
        ),
        "expected": [None, None, 12.0],
    },
    {
        "description": "Multiple trips average",
        "run": lambda: solution(
            ["checkIn", "checkOut", "checkIn", "checkOut", "getAverageTime"],
            [[1, "A", 0], [1, "B", 10], [2, "A", 5], [2, "B", 20], ["A", "B"]]
        ),
        "expected": [None, None, None, None, 12.5],
    },
    {
        "description": "Different routes",
        "run": lambda: solution(
            ["checkIn", "checkOut", "checkIn", "checkOut", "getAverageTime",
             "getAverageTime"],
            [[1, "A", 0], [1, "B", 10], [2, "C", 5], [2, "D", 20],
             ["A", "B"], ["C", "D"]]
        ),
        "expected": [None, None, None, None, 10.0, 15.0],
    },
    {
        "description": "Three trips same route",
        "run": lambda: solution(
            ["checkIn", "checkOut", "checkIn", "checkOut", "checkIn", "checkOut",
             "getAverageTime"],
            [[1, "X", 0], [1, "Y", 10], [2, "X", 0], [2, "Y", 20],
             [3, "X", 0], [3, "Y", 30], ["X", "Y"]]
        ),
        "expected": [None, None, None, None, None, None, 20.0],
    },
]
