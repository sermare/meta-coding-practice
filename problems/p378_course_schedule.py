DESCRIPTION = """
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first to
take course ai.

Return true if you can finish all courses. Otherwise, return false.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs are unique.

Examples:
  Input: numCourses = 2, prerequisites = [[1, 0]]
  Output: True

  Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
  Output: False
"""

def solution(numCourses, prerequisites):
    """
    Determine if all courses can be finished.

    Args:
        numCourses: int, total number of courses.
        prerequisites: List[List[int]], prerequisite pairs.

    Returns:
        Boolean, True if all courses can be finished.
    """
    return None
