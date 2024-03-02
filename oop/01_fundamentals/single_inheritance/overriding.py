""" Introduction to Python overridding method """

# The overriding method allows a child class to provide a specific implementation of a method 
# that is already provided by one of its parent classes.
class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self._base_pay = base_pay

    @property
    def get_pay(self):
        return self._base_pay

emp = Employee('Asad Hussain', 20_000)
print(emp._base_pay)

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive=None):
        self.name = name
        self._base_pay = base_pay
        self.sales_incentive = sales_incentive

    @property
    def get_pay(self):
        return self._base_pay + self.sales_incentive

sales = SalesEmployee('Asad Hussain', 30_000, 15_000)
print(sales.get_pay)

# The get_pay() property returns only the base_pay, not the sum of the base_pay and sales_incentive.

# When you call the get_pay() from the instance of the SalesEmployee class, 
# Python executes the get_pay() method of the Employee class, which returns the base_pay.

emp = Employee('Asad Hussain', 10_000)
print(emp.get_pay)
sales = SalesEmployee('Asad Hussain', 45_000, 5_000)
print(sales.get_pay)
# When you call the get_pay() method of the SalesEmployee‘s object, Python will call the 
# get_pay() method in the SalesEmployee class:
# If you create an instance of the Employee class, Python will call the get_pay() method of 
# the Employee class, not the get_pay() method of the SalesEmployee class. For example:

""" Advanced method overriding example """
import re
class Parser:
    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(r'\d{3}-\d{3}-\d{4}', self.text)
        if match:
            return match.group(0)
        return None

    def parse(self):
        return {
            'email': self.email(),
            'phone': self.phone()
        }

string = 'Contact us via 408-205-5663 or email@test.com'
parser = Parser(string)
print(parser.parse())

# Suppose you need to extract phone numbers in the format n-nnn-nnn-nnnn, which is the UK phone 
# number format. Also, you want to use extract email like the Parser class
# To do it, you can define a new class called UkParser that inherits from the Parser class. 
# In the UkParser class, you override the phone() method as follows:
class UkParser(Parser):
    def phone(self):
        match = re.search(r'(\+\d{1}-\d{3}-\d{3}-\d{4})', self.text)
        if match:
            return match.group(0)
        return None

string = 'Contact me via +1-650-453-3456 or email@test.co.uk'
parser = UkParser(string)
print(parser.parse())

""" Overriding attributes """
class Parser:
    phone_pattern = r'\d{3}-\d{3}-\d{4}'

    def __init__(self, text):
        self.text = text
    
    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(self.phone_pattern, self.text)
        if match:
            return match.group(0)
        return None

    def parser(self):
        return {
            'email': self.email(),
            'phone': self.phone()
        }
    
class UkParser(Parser):
    phone_pattern = '(\+\d{1}-\d{3}-\d{3}-\d{4})'

str_default = 'Contact us via 408-205-5663 or email@test.com'
str_uk = 'Contact me via +1-650-453-3456 or email@test.co.uk'
parser = Parser(str_default)
print('parser: ', parser.parser())
parser = UkParser(str_uk)
print('parser: ', parser.parser())

""" Summary """
# Method overrding allows a child class to provide a specific implementation of a method that 
# is already provided by one of its parent class.