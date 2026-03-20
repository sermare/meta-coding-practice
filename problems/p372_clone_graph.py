DESCRIPTION = """
Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node in the graph contains a value (int) and a list
of its neighbors.

The graph is represented as an adjacency list where the index of each list
represents a node (1-indexed), and each element is a list of its neighbor nodes.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops.
- The graph is connected and all nodes can be visited from the given node.

Examples:
  Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
  Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

  Input: adjList = [[]]
  Output: [[]]

  Input: adjList = []
  Output: []
"""

def solution(adjList):
    """
    Clone a graph given as adjacency list. Returns adjacency list of clone.

    Args:
        adjList: List[List[int]], adjacency list representation.

    Returns:
        List[List[int]], adjacency list of the cloned graph.
    """
    return None
