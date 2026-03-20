DESCRIPTION = """
Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates there is an edge between ai and bi.

Return the number of connected components in the graph.

Constraints:
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- No repeated edges.

Examples:
  Input: n = 5, edges = [[0,1],[1,2],[3,4]]
  Output: 2

  Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
  Output: 1
"""

def solution(n, edges):
    """
    Return the number of connected components.

    Args:
        n: int, number of nodes.
        edges: List[List[int]], the edges.

    Returns:
        An integer, number of connected components.
    """
    return None
