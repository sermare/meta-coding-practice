from problems.p009_palindrome_linked_list import solution, list_to_linked

TEST_CASES = [
    {
        "description": "Even palindrome: [1,2,2,1]",
        "run": lambda: solution(list_to_linked([1, 2, 2, 1])),
        "expected": True,
    },
    {
        "description": "Not a palindrome: [1,2]",
        "run": lambda: solution(list_to_linked([1, 2])),
        "expected": False,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution(list_to_linked([1])),
        "expected": True,
    },
    {
        "description": "Odd palindrome: [1,2,3,2,1]",
        "run": lambda: solution(list_to_linked([1, 2, 3, 2, 1])),
        "expected": True,
    },
    {
        "description": "Even longer palindrome: [1,2,3,3,2,1]",
        "run": lambda: solution(list_to_linked([1, 2, 3, 3, 2, 1])),
        "expected": True,
    },
]
