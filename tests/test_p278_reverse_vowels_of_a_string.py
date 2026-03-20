from problems.p278_reverse_vowels_of_a_string import solution

TEST_CASES = [
    {
        "description": "'hello' -> 'holle'",
        "run": lambda: solution("hello"),
        "expected": "holle",
    },
    {
        "description": "'leetcode' -> 'leotcede'",
        "run": lambda: solution("leetcode"),
        "expected": "leotcede",
    },
    {
        "description": "'aA' -> 'Aa'",
        "run": lambda: solution("aA"),
        "expected": "Aa",
    },
    {
        "description": "'xyz' -> 'xyz' (no vowels)",
        "run": lambda: solution("xyz"),
        "expected": "xyz",
    },
    {
        "description": "'aeiou' -> 'uoiea'",
        "run": lambda: solution("aeiou"),
        "expected": "uoiea",
    },
]
