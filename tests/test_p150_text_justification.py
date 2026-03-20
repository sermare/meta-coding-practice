from problems.p150_text_justification import solution

TEST_CASES = [
    {
        "description": "Standard justification",
        "run": lambda: solution(["This", "is", "an", "example", "of", "text", "justification."], 16),
        "expected": ["This    is    an", "example  of text", "justification.  "],
    },
    {
        "description": "Single word per line",
        "run": lambda: solution(["What","must","be","acknowledgment","shall","be"], 16),
        "expected": ["What   must   be", "acknowledgment  ", "shall be        "],
    },
    {
        "description": "Longer example",
        "run": lambda: solution(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
        "expected": ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "],
    },
    {
        "description": "Single word",
        "run": lambda: solution(["hello"], 10),
        "expected": ["hello     "],
    },
]
