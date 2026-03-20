from problems.p293_next_greater_element_i import solution

TEST_CASES = [
    {
        "description": "nums1=[4,1,2] nums2=[1,3,4,2] -> [-1,3,-1]",
        "run": lambda: solution([4, 1, 2], [1, 3, 4, 2]),
        "expected": [-1, 3, -1],
    },
    {
        "description": "nums1=[2,4] nums2=[1,2,3,4] -> [3,-1]",
        "run": lambda: solution([2, 4], [1, 2, 3, 4]),
        "expected": [3, -1],
    },
    {
        "description": "nums1=[1] nums2=[1] -> [-1]",
        "run": lambda: solution([1], [1]),
        "expected": [-1],
    },
    {
        "description": "nums1=[1,3,5] nums2=[6,5,4,3,2,1,7] -> [7,7,7]",
        "run": lambda: solution([1, 3, 5], [6, 5, 4, 3, 2, 1, 7]),
        "expected": [7, 7, 7],
    },
]
