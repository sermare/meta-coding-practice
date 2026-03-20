from problems.p322_goat_latin import solution

TEST_CASES = [
    {
        "description": "Basic: I speak Goat Latin",
        "run": lambda: solution("I speak Goat Latin"),
        "expected": "Imaa speakmaaa Goatmaaaa Latinmaaaaa",
    },
    {
        "description": "Vowel start: Each word",
        "run": lambda: solution("Each word"),
        "expected": "Eachmaa ordwmaaa",
    },
    {
        "description": "Single word vowel",
        "run": lambda: solution("apple"),
        "expected": "applemaa",
    },
    {
        "description": "Single word consonant",
        "run": lambda: solution("goat"),
        "expected": "oatgmaa",
    },
]
