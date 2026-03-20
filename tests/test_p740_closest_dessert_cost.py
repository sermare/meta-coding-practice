from problems.p740_closest_dessert_cost import solution

TEST_CASES = [
    {
        "description": "Exact match: baseCosts=[1,7], toppingCosts=[3,4], target=10",
        "run": lambda: solution([1, 7], [3, 4], 10),
        "expected": 10,
    },
    {
        "description": "Closest lower: baseCosts=[2,3], toppingCosts=[4,5,100], target=18",
        "run": lambda: solution([2, 3], [4, 5, 100], 18),
        "expected": 17,
    },
    {
        "description": "No toppings: baseCosts=[3,10], toppingCosts=[2,5], target=9",
        "run": lambda: solution([3, 10], [2, 5], 9),
        "expected": 8,
    },
    {
        "description": "Single base: baseCosts=[10], toppingCosts=[], target=1",
        "run": lambda: solution([10], [], 1),
        "expected": 10,
    },
]
