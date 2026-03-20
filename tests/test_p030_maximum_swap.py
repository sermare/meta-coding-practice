from problems.p030_maximum_swap import solution

TEST_CASES = [
    {
        "description": "Swap 2 and 7 in 2736 to get 7236",
        "run": lambda: solution(2736),
        "expected": 7236,
    },
    {
        "description": "9973 is already maximum, no swap needed",
        "run": lambda: solution(9973),
        "expected": 9973,
    },
    {
        "description": "Swap in 98368 to get 98863",
        "run": lambda: solution(98368),
        "expected": 98863,
    },
    {
        "description": "Swap in 1993 to get 9913",
        "run": lambda: solution(1993),
        "expected": 9913,
    },
    {
        "description": "10 stays 10 (swapping gives 01 = 1 which is less)",
        "run": lambda: solution(10),
        "expected": 10,
    },
]
