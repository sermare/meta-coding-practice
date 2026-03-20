from problems.p152_fizz_buzz import solution

TEST_CASES = [
    {
        "description": "n=3",
        "run": lambda: solution(3),
        "expected": ["1", "2", "Fizz"],
    },
    {
        "description": "n=5",
        "run": lambda: solution(5),
        "expected": ["1", "2", "Fizz", "4", "Buzz"],
    },
    {
        "description": "n=15 includes FizzBuzz",
        "run": lambda: solution(15),
        "expected": ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"],
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": ["1"],
    },
]
