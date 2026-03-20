from problems.p167_find_median_from_data_stream import solution

TEST_CASES = [
    {
        "description": "Basic median operations",
        "run": lambda: solution(["addNum","addNum","findMedian","addNum","findMedian"], [[1],[2],[],[3],[]]),
        "expected": [None, None, 1.5, None, 2.0],
    },
    {
        "description": "Single element",
        "run": lambda: solution(["addNum","findMedian"], [[5],[]]),
        "expected": [None, 5.0],
    },
    {
        "description": "Even count median",
        "run": lambda: solution(["addNum","addNum","findMedian"], [[1],[3],[]]),
        "expected": [None, None, 2.0],
    },
    {
        "description": "Multiple adds then median",
        "run": lambda: solution(["addNum","addNum","addNum","addNum","findMedian"], [[1],[2],[3],[4],[]]),
        "expected": [None, None, None, None, 2.5],
    },
]
