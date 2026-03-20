DESCRIPTION = """
Course Schedule II

There are a total of numCourses courses. You are given an array prerequisites
where prerequisites[i] = [ai, bi] indicates that you must take course bi first
to take course ai.

Return the ordering of courses you should take to finish all courses. If there
are many valid answers, return any of them. If it is impossible to finish all
courses, return an empty array.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All pairs are unique.

Examples:
  Input: numCourses = 2, prerequisites = [[1, 0]]
  Output: [0, 1]

  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0, 1, 2, 3] or [0, 2, 1, 3]

  Input: numCourses = 1, prerequisites = []
  Output: [0]
"""

def solution(numCourses, prerequisites):
    """
    Return an ordering of courses to finish all, or [] if impossible.

    Args:
        numCourses: int, total number of courses.
        prerequisites: List[List[int]], prerequisite pairs.

    Returns:
        A list of integers, valid course order or empty list.
    """
    return None
