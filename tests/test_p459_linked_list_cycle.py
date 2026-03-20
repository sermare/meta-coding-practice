from problems.p459_linked_list_cycle import solution, ListNode

TEST_CASES = [
    {
        "description": "Cycle at pos 1: [3,2,0,-4]",
        "run": lambda: solution((lambda: (lambda nodes: (nodes[-1].__setattr__('next', nodes[1]), nodes[0]))([ ListNode(v) for v in [3,2,0,-4] ] if True else None))()[1] if True else None),
        "expected": True,
    },
    {
        "description": "Cycle at pos 0: [1,2]",
        "run": lambda: solution((lambda: (lambda nodes: (nodes[-1].__setattr__('next', nodes[0]), nodes[0]))([ ListNode(v) for v in [1,2] ] if True else None))()[1] if True else None),
        "expected": True,
    },
    {
        "description": "No cycle: [1]",
        "run": lambda: solution(ListNode(1)),
        "expected": False,
    },
    {
        "description": "Empty list: no cycle",
        "run": lambda: solution(None),
        "expected": False,
    },
    {
        "description": "No cycle: [1,2,3,4]",
        "run": lambda: solution((lambda: (lambda nodes: ([ nodes[i].__setattr__('next', nodes[i+1]) for i in range(len(nodes)-1) ], nodes[0]))([ ListNode(v) for v in [1,2,3,4] ]))()[1] if True else None),
        "expected": False,
    },
]
