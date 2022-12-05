"""
ABCXYZ company has up to 100 employees.
"""


import collections

class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)

if __name__ == "__main__":
    employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
    id = 1
    print(Solution().getImportance(employees, id))