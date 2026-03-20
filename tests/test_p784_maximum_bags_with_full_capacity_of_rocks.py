from problems.p784_maximum_bags_with_full_capacity_of_rocks import solution

TEST_CASES = [
    {
        "description": "Basic: capacity=[2,3,4,5], rocks=[1,2,4,4], additional=2",
        "run": lambda: solution([2,3,4,5], [1,2,4,4], 2),
        "expected": 3,
    },
    {
        "description": "Already full: [10,2,2], rocks=[10,2,2], additional=0",
        "run": lambda: solution([10,2,2], [10,2,2], 0),
        "expected": 3,
    },
    {
        "description": "None can be filled: [100], rocks=[0], additional=1",
        "run": lambda: solution([100], [0], 1),
        "expected": 0,
    },
    {
        "description": "Fill all: [1,1,1], rocks=[0,0,0], additional=3",
        "run": lambda: solution([1,1,1], [0,0,0], 3),
        "expected": 3,
    },
]
