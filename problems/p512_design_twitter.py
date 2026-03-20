DESCRIPTION = """Design Twitter

Design a simplified version of Twitter with the following operations:
- Twitter() initializes the object.
- postTweet(userId, tweetId) composes a new tweet with ID tweetId by the user userId.
- getNewsFeed(userId) retrieves the 10 most recent tweet IDs in the user's news feed
  (including their own tweets and those from followed users), ordered from most recent
  to least recent.
- follow(followerId, followeeId) the user followerId follows the user followeeId.
- unfollow(followerId, followeeId) the user followerId unfollows the user followeeId.

Example:
    Input: ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
           [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
    Output: [None, None, [5], None, None, [6,5], None, [5]]
"""


def solution(operations, arguments):
    return None
