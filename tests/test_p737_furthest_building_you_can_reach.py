from problems.p737_furthest_building_you_can_reach import solution

TEST_CASES = [
    {
        "description": "Basic case: heights=[4,2,7,6,9,14,12], bricks=5, ladders=1",
        "run": lambda: solution([4, 2, 7, 6, 9, 14, 12], 5, 1),
        "expected": 4,
    },
    {
        "description": "All ladders: heights=[4,12,2,7,3,18,20,3,19], bricks=10, ladders=2",
        "run": lambda: solution([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2),
        "expected": 7,
    },
    {
        "description": "No climbs needed: [5,4,3,2,1]",
        "run": lambda: solution([5, 4, 3, 2, 1], 0, 0),
        "expected": 4,
    },
    {
        "description": "Single building: [1]",
        "run": lambda: solution([1], 0, 0),
        "expected": 0,
    },
]
