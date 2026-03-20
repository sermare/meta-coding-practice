DESCRIPTION = """
Evaluate Division

You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation
Ai / Bi = values[i].

You are also given some queries, where queries[j] = [Cj, Dj] represents a
query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= queries.length <= 20
- queries[j].length == 2
- 1 <= Ai.length, Bi.length, Cj.length, Dj.length <= 5

Examples:
  Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
         queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
  Output: [6.0, 0.5, -1.0, 1.0, -1.0]
"""

def solution(equations, values, queries):
    """
    Evaluate division queries using known equations.

    Args:
        equations: List[List[str]], variable pairs.
        values: List[float], equation results.
        queries: List[List[str]], queries to evaluate.

    Returns:
        A list of floats, answers to queries.
    """
    return None
