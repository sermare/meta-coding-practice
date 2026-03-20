DESCRIPTION = """Accounts Merge

Given a list of accounts where each element accounts[i] is a list of
strings, where the first element accounts[i][0] is a name, and the rest
of the elements are emails representing emails of the account.

Merge accounts that share at least one common email. After merging, return
the accounts in the format: the first element is the name, and the rest are
sorted emails. The accounts can be returned in any order.

Example:
    Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                       ["John","johnsmith@mail.com","john00@mail.com"],
                       ["Mary","mary@mail.com"],
                       ["John","johnnybravo@mail.com"]]
    Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
             ["Mary","mary@mail.com"],
             ["John","johnnybravo@mail.com"]]
"""


def solution(accounts):
    return None
