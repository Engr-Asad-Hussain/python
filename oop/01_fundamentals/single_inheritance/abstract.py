""" Introduction to Python Abstract Classes """

# In object-oriented programming, an abstract class is a class that cannot be instantiated. 
# However, you can create classes that inherit from an abstract class.

# Typically, you use an abstract class to create a blueprint for other classes.
# Similarly, an abstract method is an method without an implementation. An abstract class may 
# or may not include abstract methods.
# Python doesn’t directly support abstract classes. But it does offer a module that allows you 
# to define abstract classes.
# To define an abstract class, you use the abc (abstract base class) module.

""" Python abstract class example """

# Suppose that you need to develop a payroll program for a company.
# The company has two groups of employees: 
# # # full-time employees.
# # # hourly employees. 
# The full-time employees get a fixed salary while the hourly employees get paid by hourly 
# wages for their services.

# The payroll program needs to print out a payroll that includes employee names and their 
# monthly salaries.

# To model the payroll program in an object-oriented way, you may come up with the following 
# classes: Employee, FulltimeEmployee, HourlyEmployee, and Payroll.
from abc import abstractmethod
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @abstractmethod
    def get_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self._salary = salary
    
    def get_salary(self):
        return self._salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate=15):
        super().__init__(first_name, last_name)
        self.worked_hour = worked_hours
        self.rate = rate
    
    def get_salary(self):
        return self.worked_hour * self.rate

# The Payroll class will have a method that adds an employee to the employee list 
# and print out the payroll.
class Payroll:
    def __init__(self):
        self.emp_list = []
    
    def add(self, employees):
        self.emp_list.append(employees)

    def print(self):
        for emp in self.emp_list:
            print(f"{emp.fullname}, \t${emp.get_salary()}")

payroll = Payroll()
payroll.add(FulltimeEmployee('Asad', 'Hussain', 20_000))
payroll.add(FulltimeEmployee('Jane', 'Hussain', 30_000))
payroll.add(HourlyEmployee('John', 'Hussain', 40_000))
payroll.add(HourlyEmployee('Pope', 'Hussain', 50_000))

payroll.print()
