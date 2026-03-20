DESCRIPTION = """Critical Connections in a Network

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server
connections forming a network where connections[i] = [ai, bi] represents a connection
between servers ai and bi. Any server can reach other servers directly or indirectly
through the network.

A critical connection is a connection that, if removed, will make some servers unable
to reach some other server.

Return all critical connections in the network in any order.

Example:
    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.

Constraints:
- 2 <= n <= 10^5
- n - 1 <= connections.length <= 10^5
- 0 <= ai, bi <= n - 1
- ai != bi
- There are no repeated connections.
"""


def solution(n, connections):
    return None
