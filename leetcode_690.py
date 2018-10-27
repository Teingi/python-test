#leetcode 690. 员工的重要性

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        sum=0
        for employee in employees:
            if id==employee.id:
                sum+=employee.importance
                for subordinate in employee.subordinates:
                    sum+=self.getImportance(employees,subordinate)
        return sum
