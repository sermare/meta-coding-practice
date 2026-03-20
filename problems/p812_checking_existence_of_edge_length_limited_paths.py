DESCRIPTION = """Checking Existence of Edge Length Limited Paths

An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
[ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to
determine for each queries[j] whether there is a path between pj and qj such
that each edge on the path has a distance strictly less than limitj.

Return a boolean array answer where answer[j] is the answer to the jth query.

Example:
    Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
    Output: [False, True]

"""


def solution(n, edgeList, queries):
    return None
