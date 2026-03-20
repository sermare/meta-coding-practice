DESCRIPTION = """
Problem 15: Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph.

Each node in the graph contains a value (int) and a list of its neighbors.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The graph is connected and all nodes can be visited starting from the given node.

Examples:
  Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
  Output: [[2,4],[1,3],[2,4],[1,3]]
  Explanation: The graph has 4 nodes. The clone should have the same structure
  but with entirely new node objects.

  Input: adjList = [[]]
  Output: [[]]
  Explanation: Single node with no neighbors.

  Input: adjList = []
  Output: []
  Explanation: Null graph.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list):
    """Build a graph from an adjacency list. Returns the first node, or None if empty."""
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def solution(node):
    """
    Deep copy an undirected graph.

    Args:
        node: Node, a reference to a node in the graph.

    Returns:
        Node, the cloned graph's corresponding node.
    """
    return None
