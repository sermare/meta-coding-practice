DESCRIPTION = """
Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no
cycles. You are given a graph that started as a tree with n nodes, with one
additional edge added. The added edge has two different vertices chosen from
1 to n, and is not an edge that already exists.

The graph is represented as an array edges of length n where
edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi.

Return an edge that can be removed so that the resulting graph is a tree. If
there are multiple answers, return the answer that occurs last in the input.

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

Examples:
  Input: edges = [[1,2],[1,3],[2,3]]
  Output: [2,3]

  Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
  Output: [1,4]
"""

def solution(edges):
    """
    Find the redundant connection in the graph.

    Args:
        edges: List[List[int]], the edges of the graph.

    Returns:
        A list of two integers, the redundant edge.
    """
    return None
