from problems.p451_add_two_numbers import solution, list_to_linked, linked_to_list

TEST_CASES = [
    {
        "description": "Standard case: 342+465=807",
        "run": lambda: linked_to_list(solution(list_to_linked([2,4,3]), list_to_linked([5,6,4]))),
        "expected": [7,0,8],
    },
    {
        "description": "Both zeros: 0+0=0",
        "run": lambda: linked_to_list(solution(list_to_linked([0]), list_to_linked([0]))),
        "expected": [0],
    },
    {
        "description": "Carry propagation: 9999999+9999=10009998",
        "run": lambda: linked_to_list(solution(list_to_linked([9,9,9,9,9,9,9]), list_to_linked([9,9,9,9]))),
        "expected": [8,9,9,9,0,0,0,1],
    },
    {
        "description": "Single digits: 5+5=10",
        "run": lambda: linked_to_list(solution(list_to_linked([5]), list_to_linked([5]))),
        "expected": [0,1],
    },
    {
        "description": "Different lengths: 99+1=100",
        "run": lambda: linked_to_list(solution(list_to_linked([9,9]), list_to_linked([1]))),
        "expected": [0,0,1],
    },
]
