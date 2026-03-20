DESCRIPTION = """Number of Restricted Paths From First to Last Node

There is an undirected weighted connected graph with n nodes labeled from 1 to n.
You are given edges where edges[i] = [ui, vi, weighti] denotes an edge between
ui and vi with weight weighti.

Define distanceToLastNode(x) as the shortest distance from node x to node n.
A restricted path is a path that also satisfies that
distanceToLastNode(zi) > distanceToLastNode(zi+1) for every consecutive pair.

Return the number of restricted paths from node 1 to node n, modulo 10^9 + 7.

Example:
    Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
    Output: 3

"""


def solution(n, edges):
    return None
