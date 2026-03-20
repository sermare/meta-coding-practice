DESCRIPTION = """
Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly
one path. Given a tree of n nodes labelled from 0 to n - 1, and an array of
edges, choose any node as root to create a rooted tree. The root with the
minimum height is called a Minimum Height Tree (MHT).

Return a list of all MHTs' root labels. You can return the answer in any order.

Constraints:
- 1 <= n <= 2 * 10^4
- edges.length == n - 1
- 0 <= ai, bi < n
- ai != bi
- All the pairs are unique.
- The given input is guaranteed to be a tree.

Examples:
  Input: n = 4, edges = [[1,0],[1,2],[1,3]]
  Output: [1]

  Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
  Output: [3, 4]

  Input: n = 1, edges = []
  Output: [0]
"""

def solution(n, edges):
    """
    Find all roots that produce minimum height trees.

    Args:
        n: int, number of nodes.
        edges: List[List[int]], tree edges.

    Returns:
        A list of integers, MHT root labels.
    """
    return None
