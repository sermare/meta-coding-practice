from problems.p673_wiggle_sort import solution


def _is_wiggle_sorted(nums):
    for i in range(1, len(nums)):
        if i % 2 == 1 and nums[i] < nums[i - 1]:
            return False
        if i % 2 == 0 and nums[i] > nums[i - 1]:
            return False
    return True


TEST_CASES = [
    {
        "description": "Basic case: [3,5,2,1,6,4]",
        "run": lambda: _is_wiggle_sorted(solution([3, 5, 2, 1, 6, 4])),
        "expected": True,
    },
    {
        "description": "Already sorted: [1,2,3]",
        "run": lambda: _is_wiggle_sorted(solution([1, 2, 3])),
        "expected": True,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Two elements: [2,1]",
        "run": lambda: _is_wiggle_sorted(solution([2, 1])),
        "expected": True,
    },
]
