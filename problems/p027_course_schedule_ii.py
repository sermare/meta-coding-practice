DESCRIPTION = """
Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you
want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.

Return the ordering of courses you should take to finish all courses. If there
are multiple valid answers, return any of them. If it is impossible to finish
all courses, return an empty array.

Constraints:
  - 1 <= numCourses <= 2000
  - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
  - prerequisites[i].length == 2
  - 0 <= ai, bi < numCourses
  - ai != bi
  - All the pairs [ai, bi] are distinct.

Examples:
  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: [0,1]

  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0,2,1,3] (or any valid topological order)

  Input: numCourses = 1, prerequisites = []
  Output: [0]
""".strip()


def solution(numCourses: int, prerequisites):
    return None
