from problems.p512_design_twitter import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"], [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]),
        "expected": [None, None, [5], None, None, [6, 5], None, [5]],
    },
    {
        "description": "Empty feed",
        "run": lambda: solution(["Twitter","getNewsFeed"], [[],[1]]),
        "expected": [None, []],
    },
    {
        "description": "Self tweets only",
        "run": lambda: solution(["Twitter","postTweet","postTweet","getNewsFeed"], [[],[1,1],[1,2],[1]]),
        "expected": [None, None, None, [2, 1]],
    },
    {
        "description": "Follow then post",
        "run": lambda: solution(["Twitter","follow","postTweet","getNewsFeed"], [[],[1,2],[2,10],[1]]),
        "expected": [None, None, None, [10]],
    },
]
