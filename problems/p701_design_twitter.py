DESCRIPTION = """Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow
another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- postTweet(userId, tweetId) Composes a new tweet with ID tweetId by the user userId.
- getNewsFeed(userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
  Each item must be posted by users who the user followed or by the user themselves.
  Tweets must be ordered from most recent to least recent.
- follow(followerId, followeeId) The user with ID followerId started following the
  user with ID followeeId.
- unfollow(followerId, followeeId) The user with ID followerId unfollowed the user
  with ID followeeId.

Example:
    Input: twitter = Twitter()
           twitter.postTweet(1, 5)
           twitter.getNewsFeed(1)
    Output: [5]
"""


def solution():
    return None
