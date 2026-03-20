from problems.p513_find_median_from_data_stream import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution(["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"], [[],[1],[2],[],[3],[]]),
        "expected": [None, None, None, 1.5, None, 2.0],
    },
    {
        "description": "Single element",
        "run": lambda: solution(["MedianFinder","addNum","findMedian"], [[],[5],[]]),
        "expected": [None, None, 5.0],
    },
    {
        "description": "Even count",
        "run": lambda: solution(["MedianFinder","addNum","addNum","findMedian"], [[],[1],[3],[]]),
        "expected": [None, None, None, 2.0],
    },
    {
        "description": "Negative numbers",
        "run": lambda: solution(["MedianFinder","addNum","addNum","addNum","findMedian"], [[],[-1],[-2],[-3],[]]),
        "expected": [None, None, None, None, -2.0],
    },
    {
        "description": "Duplicates",
        "run": lambda: solution(["MedianFinder","addNum","addNum","addNum","findMedian"], [[],[5],[5],[5],[]]),
        "expected": [None, None, None, None, 5.0],
    },
]
