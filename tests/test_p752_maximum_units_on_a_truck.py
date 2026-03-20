from problems.p752_maximum_units_on_a_truck import solution

TEST_CASES = [
    {
        "description": "Basic case: [[1,3],[2,2],[3,1]], truckSize=4",
        "run": lambda: solution([[1,3],[2,2],[3,1]], 4),
        "expected": 8,
    },
    {
        "description": "All boxes fit: [[5,10],[2,5],[4,7],[3,9]], truckSize=10",
        "run": lambda: solution([[5,10],[2,5],[4,7],[3,9]], 10),
        "expected": 91,
    },
    {
        "description": "Single box type: [[3,5]], truckSize=3",
        "run": lambda: solution([[3,5]], 3),
        "expected": 15,
    },
    {
        "description": "Truck size zero",
        "run": lambda: solution([[1,3],[2,2]], 0),
        "expected": 0,
    },
    {
        "description": "Large truck: [[2,1],[3,3]], truckSize=100",
        "run": lambda: solution([[2,1],[3,3]], 100),
        "expected": 11,
    },
]
