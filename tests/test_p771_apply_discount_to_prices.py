from problems.p771_apply_discount_to_prices import solution

TEST_CASES = [
    {
        "description": "Basic discount: 50%",
        "run": lambda: solution("there are $1 $2 and 5$ candies in the shop", 50),
        "expected": "there are $0.50 $1.00 and 5$ candies in the shop",
    },
    {
        "description": "No prices",
        "run": lambda: solution("hello world", 10),
        "expected": "hello world",
    },
    {
        "description": "100% discount",
        "run": lambda: solution("$10 $20", 100),
        "expected": "$0.00 $0.00",
    },
    {
        "description": "0% discount",
        "run": lambda: solution("$100", 0),
        "expected": "$100.00",
    },
]
