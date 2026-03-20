DESCRIPTION = """Design Browser History

You have a browser of one tab where you start on the homepage and you can visit
another url, get back in the history number of steps or move forward in the
history number of steps.

Implement the BrowserHistory class:
- BrowserHistory(homepage) initializes with the homepage.
- visit(url) visits url from the current page, clears forward history.
- back(steps) moves back steps in history and returns the current url.
- forward(steps) moves forward steps in history and returns the current url.

Example:
    Input:
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")
        bh.back(1)        -> "facebook.com"
        bh.back(1)        -> "google.com"
        bh.forward(1)     -> "facebook.com"
        bh.visit("linkedin.com")
        bh.forward(2)     -> "linkedin.com"
        bh.back(2)        -> "google.com"
        bh.back(7)        -> "leetcode.com"
"""


def solution(operations, arguments):
    return None
