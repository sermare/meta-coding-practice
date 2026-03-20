DESCRIPTION = """
Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given the integer
n and a list of edges where edges[i] = [ai, bi] indicates there is an
undirected edge between nodes ai and bi.

Return true if the edges of the given graph make up a valid tree, and false
otherwise.

A valid tree has n-1 edges, is connected, and has no cycles.

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- No duplicate edges.

Examples:
  Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
  Output: True

  Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
  Output: False
"""

def solution(n, edges):
    """
    Determine if the graph forms a valid tree.

    Args:
        n: int, number of nodes.
        edges: List[List[int]], the edges.

    Returns:
        Boolean, True if valid tree.
    """
    return None
