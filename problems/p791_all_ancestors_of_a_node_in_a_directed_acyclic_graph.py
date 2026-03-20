DESCRIPTION = """All Ancestors of a Node in a Directed Acyclic Graph

You are given a positive integer n representing the number of nodes of a
Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [from_i, to_i]
denotes a unidirectional edge from from_i to to_i in the DAG.

Return a list answer, where answer[i] is the list of ancestors of the i-th node,
sorted in ascending order.

Example:
    Input: n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
"""


def solution(n, edges):
    return None
