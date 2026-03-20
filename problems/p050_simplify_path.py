DESCRIPTION = """
Simplify Path

Given an absolute path for a Unix-style file system, which begins with a slash
'/', transform this path into its simplified canonical path.

In a Unix-style file system:
- A period '.' refers to the current directory.
- A double period '..' refers to the parent directory.
- Multiple consecutive slashes '//' are treated as a single slash '/'.
- Any sequence of periods that does not match '.' or '..' is treated as a
  valid directory/file name.

The simplified canonical path should:
- Start with a single slash '/'.
- Directories are separated by a single slash '/'.
- Not end with a trailing slash '/' (unless it is the root directory).
- Not have any '.' or '..' as components of the canonical path.

Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, '.', '/' or '_'
- path is a valid absolute Unix path

Examples:
  Input: path = "/home/"
  Output: "/home"

  Input: path = "/../"
  Output: "/"

  Input: path = "/home//foo/"
  Output: "/home/foo"
"""


def solution(path):
    """
    Simplify a Unix-style absolute path to its canonical form.

    Args:
        path: str - an absolute Unix-style path

    Returns:
        str - the simplified canonical path
    """
    return None
