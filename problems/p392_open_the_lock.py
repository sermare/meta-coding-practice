DESCRIPTION = """
Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10
slots: '0' through '9'. The wheels can rotate freely and wrap around. Each
move consists of turning one wheel one slot.

The lock initially starts at '0000'. You are given a list of deadends
(combinations that will lock the lock forever) and a target representing the
value of the wheels that will unlock the lock.

Return the minimum total number of turns required to open the lock, or -1 if
it is impossible.

Constraints:
- 1 <= deadends.length <= 500
- deadends[i].length == 4
- target.length == 4
- target will not be in the list of deadends.
- target and deadends[i] consist of digits only.

Examples:
  Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
  Output: 6

  Input: deadends = ["8888"], target = "0009"
  Output: 1

  Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
  Output: -1
"""

def solution(deadends, target):
    """
    Return the minimum turns to reach the target from '0000'.

    Args:
        deadends: List[str], combinations that lock forever.
        target: str, the target combination.

    Returns:
        An integer, minimum turns or -1.
    """
    return None
