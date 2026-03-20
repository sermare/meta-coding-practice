from problems.p674_wiggle_sort_ii import solution


def _is_strict_wiggle(nums):
    for i in range(1, len(nums)):
        if i % 2 == 1 and nums[i] <= nums[i - 1]:
            return False
        if i % 2 == 0 and nums[i] >= nums[i - 1]:
            return False
    return True


TEST_CASES = [
    {
        "description": "Basic case: [1,5,1,1,6,4]",
        "run": lambda: _is_strict_wiggle(solution([1, 5, 1, 1, 6, 4])),
        "expected": True,
    },
    {
        "description": "Simple: [1,3,2,2,3,1]",
        "run": lambda: _is_strict_wiggle(solution([1, 3, 2, 2, 3, 1])),
        "expected": True,
    },
    {
        "description": "Two elements: [1,2]",
        "run": lambda: _is_strict_wiggle(solution([1, 2])),
        "expected": True,
    },
    {
        "description": "Distinct elements: [4,5,6,7]",
        "run": lambda: _is_strict_wiggle(solution([4, 5, 6, 7])),
        "expected": True,
    },
]
