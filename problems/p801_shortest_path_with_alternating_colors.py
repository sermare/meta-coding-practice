DESCRIPTION = """Shortest Path with Alternating Colors

You are given an integer n, the number of nodes in a directed graph where the
nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph.

You are given two arrays redEdges and blueEdges where:
- redEdges[i] = [ai, bi] indicates a directed red edge from node ai to node bi.
- blueEdges[i] = [uj, vj] indicates a directed blue edge from node uj to node vj.

Return an array answer of length n, where each answer[x] is the length of the
shortest path from node 0 to node x such that the edge colors alternate along
the path, or -1 if such a path does not exist.

Example:
    Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
    Output: [0,1,-1]

"""


def solution(n, redEdges, blueEdges):
    return None
