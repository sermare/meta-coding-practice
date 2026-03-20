from problems.p015_clone_graph import solution, build_graph, Node


def _graph_to_adj_list(node):
    """Convert a graph back to an adjacency list representation."""
    if node is None:
        return []
    visited = {}
    queue = [node]
    visited[node.val] = node
    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)
    adj_list = [[] for _ in range(len(visited))]
    for val in sorted(visited.keys()):
        adj_list[val - 1] = sorted([n.val for n in visited[val].neighbors])
    return adj_list


def _collect_nodes(node):
    """Collect all node objects reachable from the given node."""
    if node is None:
        return set()
    visited = set()
    queue = [node]
    while queue:
        current = queue.pop(0)
        if id(current) in visited:
            continue
        visited.add(id(current))
        for neighbor in current.neighbors:
            queue.append(neighbor)
    return visited


def _validate_clone(adj_list):
    """Build graph, clone it, and verify structure matches and objects are different."""
    original = build_graph(adj_list)
    clone = solution(original)

    if original is None:
        return clone is None

    # Check structure matches
    original_adj = _graph_to_adj_list(original)
    clone_adj = _graph_to_adj_list(clone)
    if original_adj != clone_adj:
        return False

    # Check that no objects are shared
    original_ids = _collect_nodes(original)
    clone_ids = _collect_nodes(clone)
    if original_ids & clone_ids:
        return False

    return True


TEST_CASES = [
    {
        "description": "4-node graph: [[2,4],[1,3],[2,4],[1,3]]",
        "run": lambda: _validate_clone([[2, 4], [1, 3], [2, 4], [1, 3]]),
        "expected": True,
    },
    {
        "description": "Single node with no neighbors: [[]]",
        "run": lambda: _validate_clone([[]]),
        "expected": True,
    },
    {
        "description": "Empty graph: []",
        "run": lambda: _validate_clone([]),
        "expected": True,
    },
]
