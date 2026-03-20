from problems.p465_flatten_a_multilevel_doubly_linked_list import solution, Node, flatten_to_list

def _build_case1():
    """Build: 1-2-3-4-5-6 with 3->child->7-8-9-10, 8->child->11-12"""
    nodes = {i: Node(i) for i in range(1, 13)}
    # Level 1: 1-2-3-4-5-6
    for i in range(1, 6):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    # Level 2: 7-8-9-10 (child of 3)
    nodes[3].child = nodes[7]
    for i in range(7, 10):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    # Level 3: 11-12 (child of 8)
    nodes[8].child = nodes[11]
    nodes[11].next = nodes[12]
    nodes[12].prev = nodes[11]
    return nodes[1]


def _build_case2():
    """Build: 1-2 with 1->child->3"""
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.next = n2
    n2.prev = n1
    n1.child = n3
    return n1


TEST_CASES = [
    {
        "description": "Multilevel: [1,2,3,4,5,6] with children",
        "run": lambda: flatten_to_list(solution(_build_case1())),
        "expected": [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6],
    },
    {
        "description": "Simple child: 1->child->3, 1->next->2",
        "run": lambda: flatten_to_list(solution(_build_case2())),
        "expected": [1, 3, 2],
    },
    {
        "description": "Single node no child",
        "run": lambda: flatten_to_list(solution(Node(1))),
        "expected": [1],
    },
    {
        "description": "Empty list",
        "run": lambda: flatten_to_list(solution(None)),
        "expected": [],
    },
]
