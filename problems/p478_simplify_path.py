DESCRIPTION = """Simplify Path

Given an absolute path for a Unix-style file system, which begins with a slash '/',
transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' refers to the current directory,
a double period '..' moves up a directory, and any multiple consecutive slashes '//'
are treated as a single slash '/'.

The simplified canonical path should adhere to the following rules:
    - It must start with a single slash '/'.
    - Directories within the path must be separated by exactly one slash '/'.
    - It must not end with a slash '/' unless it is the root directory.
    - It must not have any single or double periods used as directory names.

Example 1:
    Input: path = "/home/"
    Output: "/home"

Example 2:
    Input: path = "/home//foo/"
    Output: "/home/foo"

Example 3:
    Input: path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"

Example 4:
    Input: path = "/../"
    Output: "/"

Constraints:
    - 1 <= path.length <= 3000
    - path consists of English letters, digits, period '.', slash '/', or underscore '_'.
    - path is a valid absolute Unix path.
"""

def solution(path):
    return None
