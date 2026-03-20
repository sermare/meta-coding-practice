from problems.p184_find_peak_element import solution

def _is_peak(nums, idx):
    if idx < 0 or idx >= len(nums):
        return False
    left = nums[idx - 1] if idx > 0 else float('-inf')
    right = nums[idx + 1] if idx < len(nums) - 1 else float('-inf')
    return nums[idx] > left and nums[idx] > right

TEST_CASES = [
    {
        "description": "[1,2,3,1] peak at 2",
        "run": lambda: _is_peak([1,2,3,1], solution([1,2,3,1])),
        "expected": True,
    },
    {
        "description": "[1,2,1,3,5,6,4] valid peak",
        "run": lambda: _is_peak([1,2,1,3,5,6,4], solution([1,2,1,3,5,6,4])),
        "expected": True,
    },
    {
        "description": "Single element is peak",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "Ascending -> last is peak",
        "run": lambda: solution([1, 2, 3]),
        "expected": 2,
    },
]
