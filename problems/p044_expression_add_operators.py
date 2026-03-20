DESCRIPTION = """
Expression Add Operators

Given a string num that contains only digits and an integer target, return all
possibilities to insert the binary operators '+', '-', and/or '*' between the
digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Constraints:
- 1 <= num.length <= 10
- num consists of only digits
- -2^31 <= target <= 2^31 - 1

Examples:
  Input: num = "123", target = 6
  Output: ["1+2+3", "1*2*3"]

  Input: num = "232", target = 8
  Output: ["2*3+2", "2+3*2"]

  Input: num = "3456237490", target = 9191
  Output: []

  Input: num = "105", target = 5
  Output: ["1*0+5", "10-5"]
"""


def solution(num, target):
    """
    Add +, -, * between digits of num to produce expressions equaling target.

    Args:
        num: str - a string of digits
        target: int - the target value

    Returns:
        List[str] - all valid expressions that evaluate to target
    """
    return None
