DESCRIPTION = """Invalid Transactions

A transaction is possibly invalid if:
- the amount exceeds $1000, or
- if it occurs within (and including) 60 minutes of another transaction with the same
  name in a different city.

You are given a list of strings `transactions` where each transaction is formatted as
"name,time,amount,city".

Return a list of transactions that are possibly invalid. You may return the answer in
any order.

Example:
    Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    Output: ["alice,20,800,mtv","alice,50,100,beijing"]

    Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    Output: ["alice,50,1200,mtv"]
"""


def solution(transactions):
    return None
