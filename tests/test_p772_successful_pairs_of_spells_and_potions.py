from problems.p772_successful_pairs_of_spells_and_potions import solution

TEST_CASES = [
    {
        "description": "Basic: spells=[5,1,3], potions=[1,2,3,4,5], success=7",
        "run": lambda: solution([5,1,3], [1,2,3,4,5], 7),
        "expected": [4,0,3],
    },
    {
        "description": "All successful: spells=[3,1,2], potions=[8,5,8], success=3",
        "run": lambda: solution([3,1,2], [8,5,8], 3),
        "expected": [3,2,3],
    },
    {
        "description": "None successful: spells=[1], potions=[1], success=10",
        "run": lambda: solution([1], [1], 10),
        "expected": [0],
    },
    {
        "description": "Single spell: spells=[10], potions=[1,2,3], success=15",
        "run": lambda: solution([10], [1,2,3], 15),
        "expected": [2],
    },
]
