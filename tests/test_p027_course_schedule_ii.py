from problems.p027_course_schedule_ii import solution


def _is_valid_topological_order(order, numCourses, prerequisites):
    """Validate that the given order is a valid topological sort."""
    if len(order) != numCourses:
        return False
    if set(order) != set(range(numCourses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    for ai, bi in prerequisites:
        if position[bi] >= position[ai]:
            return False
    return True


def _run_test_2_courses():
    result = solution(2, [[1, 0]])
    return _is_valid_topological_order(result, 2, [[1, 0]])


def _run_test_4_courses():
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution(4, prereqs)
    return _is_valid_topological_order(result, 4, prereqs)


def _run_test_1_course():
    result = solution(1, [])
    return _is_valid_topological_order(result, 1, [])


def _run_test_cycle():
    result = solution(2, [[1, 0], [0, 1]])
    return result


TEST_CASES = [
    {
        "description": "2 courses with one prerequisite: valid topo order",
        "run": _run_test_2_courses,
        "expected": True,
    },
    {
        "description": "4 courses with multiple prerequisites: valid topo order",
        "run": _run_test_4_courses,
        "expected": True,
    },
    {
        "description": "1 course with no prerequisites: [0]",
        "run": _run_test_1_course,
        "expected": True,
    },
    {
        "description": "Cycle detected: return empty list",
        "run": _run_test_cycle,
        "expected": [],
    },
]
