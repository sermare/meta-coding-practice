DESCRIPTION = """Employees Earning More Than Their Managers

Given a list of employees where each employee has an id, name, salary, and managerId,
find the names of employees who earn more than their managers.

Each employee is represented as a dictionary with keys: 'id', 'name', 'salary', 'managerId'.
A managerId of None means the employee has no manager.

Example:
    Input: employees = [
        {"id": 1, "name": "Joe", "salary": 70000, "managerId": 3},
        {"id": 2, "name": "Henry", "salary": 80000, "managerId": 4},
        {"id": 3, "name": "Sam", "salary": 60000, "managerId": None},
        {"id": 4, "name": "Max", "salary": 90000, "managerId": None}
    ]
    Output: ["Joe"]
    Explanation: Joe earns 70000 which is more than his manager Sam who earns 60000.
"""


def solution(employees):
    return None
