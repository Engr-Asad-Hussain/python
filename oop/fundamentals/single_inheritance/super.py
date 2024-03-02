""" Introduction to the Python super """

from email.mime import base


class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentives):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        self.sales_incentives = sales_incentives

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentives

""" super().__init__() """
# The __init__() method of the SalesEmployee class has some parts that are the same as the 
# ones in the __init__() method of the Employee class.

# To avoid duplication, you can call the __init__() method of Employee class from the __init__() 
# method of the SalesEmployee class.

# To reference the Employee class in the SalesEmployee class, you use the super(). 
# The super() returns a reference of the parent class from a child class.

# The following redefines the SalesEmployee class that uses the super() to call the __init__() 
# method of the Employee class

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentives):
        super().__init__(name, base_pay, bonus)
        self.sales_incentives = sales_incentives

    def get_pay(self):
        return super().get_pay() + self.sales_incentives

emp = Employee('Asad Hussain', 25_000, 5_000)
print(emp.get_pay())

sales_emp = SalesEmployee('Ali Hussain', 55_000, 15_000, 5_000)
print(sales_emp.get_pay())

""" Summary """
# Use super() to call the methods of a parent class from a child class.