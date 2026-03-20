from problems.p850_recover_binary_search_tree import solution, build_tree

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

TEST_CASES = [
    {
        "description": "Swap 1 and 3: [1,3,None,None,2]",
        "run": lambda: tree_to_list(solution(build_tree([1, 3, None, None, 2]))),
        "expected": [3, 1, None, None, 2],
    },
    {
        "description": "Swap 2 and 3: [3,1,4,None,None,2]",
        "run": lambda: tree_to_list(solution(build_tree([3, 1, 4, None, None, 2]))),
        "expected": [2, 1, 4, None, None, 3],
    },
    {
        "description": "Two nodes: [2,1]",
        "run": lambda: tree_to_list(solution(build_tree([2, 1]))),
        "expected": [1, 2],
    },
    {
        "description": "Already correct single: [1]",
        "run": lambda: tree_to_list(solution(build_tree([1]))),
        "expected": [1],
    },
]
