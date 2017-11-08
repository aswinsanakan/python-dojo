
class Employee:
  'Example python class'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
    print "Total Employees %d" % Employee.empCount

  def displayEmployee(self):
    print "Name : ", self.name , ", Salary : ", self.salary

emp1 = Employee("Aswin", 50000)
emp1.displayEmployee()

import code ; code.interact(local=locals())

emp2 = Employee("Brad", 40000)
emp2.displayEmployee()

print "Total Employees : %d" % Employee.empCount