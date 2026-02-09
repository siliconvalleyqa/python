##
# CIS 117 - Chapter 10 Exercise 1 - Erick Ramos
#
# This program demonstrates inheritance:
# - Makes a class Employee with these instance variables: name and salary.
# - Makes a class Manager inherit from the Employee class.
# - Adds an instance variable "department" that stores a string.
# - Supplies a method __repr__ that prints the manager’s name, department, and salary.
# - Makes a class Executive inherit from the Manager class. 
# - Supplies appropriate __repr__ methods for all classes.
# - Supplies a test program that tests these classes and methods.
#

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def __repr__(self):
        # return f"Employee: {self.name}, Salary: ${self.salary}"
        return "Employee: %s, Salary: %i" % (self.name, self.salary)
    

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __repr__(self):
        return f"Manager: {self.name}, Department: {self.department}, Salary: ${self.salary}"


class Executive(Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self):
        return f"Executive: {self.name}, Dept: {self.department}, Salary: ${self.salary}"


def main():

    employee = Employee("Sherri",300000)
    print(employee)

    manager = Manager("Erick", 500000, "Engineering")
    print(manager)

    executive = Executive("Sinforiana", 750000, "Executive Visionary")
    print(executive)

if __name__ == "__main__":
    main()


##  Output 1
# Employee: Sherri, Salary: 300000
# Manager: Erick, Department: Engineering, Salary: $500000
# Executive: Sinforiana, Dept: Executive Visionary, Salary: $750000

