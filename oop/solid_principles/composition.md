## Composition: Favour composition over inheritance

Many of the design patterns in the ***Gang of Four Design Patterns*** book are based on the principle that favour composition over inheritance. But what does that mean? Let's find out. If you want to separate responsibilities (_Single Responsibility Principle by Robert C. Martin_), create code with higher cohession, there's a couple of ways to do it. 
  1. One way to do it is ***inheritance***. So instead of putting everything in one single big class, you would create a class hierarchy of classes and subclasses, where you would put certain things in a subclass so that it would be separated from the main class. 
  2. Another way you can do is ***composition***. That means that you are basically using separate classes to represent separate things in the application. And then each of these classes use each other in some meaningful way. 

Its basically the difference between the ```is-a relationship``` which is inheritance and ```has-a relationship``` which is composition; allow you to separate responsibilities.

### Explanation of an example
Consider a following advanced example of employee management system.

```py
class HourlyEmployee:
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        pay_rate: float = 0,
        hours_worked: int = 0,
        employer_cost: float = 1000,
    ) -> None:
        self.name = name
        self.id = id
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.employer_cost = employer_cost

    def compute_pay(self):
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.commission * self.contracts_landed
        )
```
We have an hourly employee who's paid based on the number of work hours. The hourly employee have some personnel data like the ```name``` and ```id```, we have a part that's about ```commission```. So if an employee lands a number of contract, the employee gets a commission, we have ```pay_rate```, number of ```hours worked```, and there is a kind of fixed ```employee cost```. And then we have ```compute pay``` method that actually computes how much the employee should be paid based on these values.

```py
class SalariedEmployee:
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        monthly_salary: float = 0,
        percentage: float = 1,
    ) -> None:
        self.name = name
        self.id = id
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def compute_pay(self):
        return (
            self.monthly_salary * self.percentage
            + self.commission * self.contracts_landed
        )
```
Salaried employee that gets a fixed monthly salary. Salaried employees quite to similar to ```HourlyEmployee```. It also has a ```name```, ```id```, it also has a ```commission``` structure. But there is a ```monthly salary``` and a ```percentage``` of time that the employee works. And then this is the ```compute pay``` method. 

```py
class FreelancerEmployee:
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        pay_rate: float = 0,
        hours_worked: int = 0,
        vat_number: str = "",
    ) -> None:
        self.name = name
        self.id = id
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.vat_number = vat_number

    def compute_pay(self):
        return (
            self.pay_rate * self.hours_worked + self.commission * self.contracts_landed
        )
```
And we have a freelancer. Freelancer is not actually an employee. But if we consider an employee as a person that gets paid by a company for work performed, and it kind of fits under that same umbrella. Freelancer also has ```name``` and ```id```, ```commission```, ```pay rate``` and ```hours worked```. And then we have an additional ```VAT number``` for taxes. 

```py
def main():
    henry = HourlyEmployee(name="Henry", id=1002, pay_rate=50, hours_worked=100)
    print(
        f"`{henry.name}` worked for `{henry.hours_worked}` hours and earned `${henry.compute_pay()}`."
    )

    sarah = SalariedEmployee(
        name="Sarah", id=2031, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"`{sarah.name}` landed `{sarah.contracts_landed}` contracts and earned `${sarah.compute_pay()}`."
    )

if __name__ == "__main__":
    main()
```
In the main function where we create a couple of these employees print out some information. And this is what happens when I run this example:
```
`Henry` worked for `100` hours and earned `$6000`.
`Sarah` landed `10` contracts and earned `$6000`.
```

### Explanation of problems
Now, let's analyse this code, there's two main problems.
> [!WARNING]
> The first problem is that there's a lot of ***code duplication***, I mean, hourly employee has Commission, contracts landed, so a salaried employee and Freelancer has this as well, there's a lot of duplication in the way that the pay is computed.

> [!WARNING]
> Another issue is that each of these classes have a ***lot of responsibilities***. For example, here, this one is responsible for storing personnel data, it's responsible for dealing with commissions, and it's responsible for the pay rate and hours worked and how to compute the pay based on that. And the same goes for the salaried employee, and for the Freelancer as well.

So two problems that we'd like to solve. And you can use inheritance to do it by basically creating a hierarchy of classes and subclasses. Or you could also use composition. And that's basically separating out the different aspects of what a class consists of, and then combining them later on.

### Technique 1: Inheritance
We're going to create a superclass for each of these employee types that store some generic data (```name```, ```id``` and ```compute_pay```) that's useful for every employee. And let's call that ```class Employee```. And we're going to turn that into an ```abstract base class```.

```py
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    @abstractmethod
    def compute_pay(self) -> float:
        pass
```

Now we have this basic employee class and then obviously hourly employee and salary employee and Freelancer are going to inherit from that. And then an hourly employee, we don't need this part anymore.

```py
class HourlyEmployee(Employee):
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        pay_rate: float = 0,
        hours_worked: int = 0,
        employer_cost: float = 1000,
    ) -> None:
        super().__init__(name, id)
        self.commission = commission
        self.contracts_landed = contracts_landed
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.employer_cost = employer_cost

    ...
```
We are going to do the same for ```SalariedEmployee``` and ```FreelancerEmployee```.
Let's verify that this still works correctly. 
```
`Henry` worked for `100` hours and earned `$6000`.
`Sarah` landed `10` contracts and earned `$6000`.
```

We've used inheritance to separate out a bit of information about employees and separated that from the rest. So for this inheritance works fine. ***But the problem is, each of these classes still have too many responsibilities.*** For example, there is both commission information and pay information. So it would be nice to also separate that out. If you want to use inheritance, what you need to do is create subclasses for each of these employee types to have a version with commission and the version without commission. 
So for example, what you could do is create a ```class SalariedEmployeeWithCommission``` that is a subclass of ```SalariedEmployee```.

```py
class SalariedEmployee(Employee):
    def __init__(
        self,
        name: str,
        id: int,
        monthly_salary: float = 0,
        percentage: float = 1,
    ) -> None:
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def compute_pay(self):
        return self.monthly_salary * self.percentage


class SalariedEmployeeWithCommission(SalariedEmployee):
    def __init__(
        self,
        name: str,
        id: int,
        commission: float = 100,
        contracts_landed: float = 0,
        monthly_salary: float = 0,
        percentage: float = 1,
    ) -> None:
        super().__init__(name, id, monthly_salary, percentage)
        self.commission = commission
        self.contracts_landed = contracts_landed

    def compute_pay(self):
        return super().compute_pay() + self.commission * self.contracts_landed
```

So we have a ```SalariedEmployeeWithCommission```. And that's a subclass of ```SalariedEmployee```.
And now what I need to do here in this main function is to make sure that ```sarah```, because Sarah is actually an employee with commission is now no longer a salaried employee, but as a salaried employee with commission.

```py
def main():
    ...
    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=2031, monthly_salary=5000, contracts_landed=10
    )
    ...
```

There we go. And let's run this code, again, we're gonna get the same result. 
```
`Henry` worked for `100` hours and earned `$6000`.
`Sarah` landed `10` contracts and earned `$6000`.
```

But now see, we use inheritance to separate these different responsibilities a bit more, if you want to do this for other employee types, because obviously, the Freelancer also has that same commission structure and the only employee also has the same commission structure, I would have to create a hourly employee with commission, that's an hourly employee subclass, and a freelancer with commission that's a freelancer subclass. 

### Problems with the inheritance technique
> [!IMPORTANT]
> You already see where this is leading to issues. Because one thing we didn't really solve is the ***code duplication***, because if you look at ```FreelancerWithCommission```, and you look at ```SalariedEmployeeWithCommission``` these classes are more or less the same. Basically, the only difference is that they're a subclass of another class. ```SalariedEmployeeWithCommission``` one is a subclass of ```SalariedEmployee```. ```FreelancerWithCommission``` is a subclass of ```Freelancer```. So code duplication, we didn't really solve.

> [!IMPORTANT]
> Another issue by doing this with inheritance that basically for every variation that we're going to add, we're going to get this ***explosion of subclasses***. For example, suppose you also want to have a yearly bonus that's included with the pay, then you would get a lots and lots of subclasses, like ```FreelancerWithCommissionWithoutBonus```, ```SalariedEmployeeWithoutCommissionWithBonus```, etc, etc. 

So in the end, that kind of approach doesn't really work. And that's also the crux of what it means when we say ```favour composition over inheritance```. If you use inheritance too much to separate the responsibilities in this way, it means you're going to end up with this huge hierarchy of subclasses and it's going to be really difficult to deal with also because ***inheritance actually introduces a lot of coupling*** because for example, here the ```FreelancerWithCommission``` uses again the ```compute_pay``` from the super class ```super().compute_pay()```, so it assumes things about what compute pay does and superclass does. That's what happens when you do this with inheritance. 

### Technique 2: Composition
let's look at another option, which is ```composition```. And with composition, we're not creating hierarchies of classes, we're trying to separate out the concepts and then combine them in meaningful ways. In this case, we have a few different concepts. Whereas the employee, with the employee data, we have the employee payment structure, which is either hourly or salaried, or on Freelancer basis. And we have the commission, which is based on the number of contracts that an employee has landed. So what you can do, instead of using inheritance to combine all these things, you could also create separate class hierarchies for each of these three different things and then combine them later on, what you could do in this example is create a commission class and a contract class and combine them with the employee class later on. 
So first thing I'm going to create a commission class. 

```py
class Commission:
    def __init__(
        self,
        commission: float = 100,
        contracts_landed: float = 0,
    ) -> None:
        self.commission = commission
        self.contracts_landed = contracts_landed

    def get_payment(self):
        return self.commission * self.contracts_landed
```

Now, let's also add a ```class Contract```. For the contract, I'm going to use an ```abstract base class``` because then we can make subclasses like hourly contract, salaried contract or freelancer contract. And the only thing that the contract class is going to have is a ```get_payment``` method. 

```py
class Contract(ABC):
    @abstractmethod
    def get_payment(self) -> float:
        pass
```

Now we have both a ```class Commission```, we have a ```class Contract```, and we have the ```class Employee```. 
And now this is where composition gets into play. Because what we can do now is basically assign these contracts and commissions to an employee. So an employee is not only going to have a ```name``` and an ```id```, but it's also going to have a ```contract```. And an employee is also going to have a ```commission```. Now, because not every employee is going to have a commission, we're going to turn this into an ```optional type```. To compute pay, we simply use the methods from the ```Contract``` and from the ```Commission``` to compute. 

```py
from typing import Optional

class Employee:
    def __init__(
        self,
        name: str,
        id: int,
        contract: Contract,
        commission: Optional[Commission] = None,
    ) -> None:
        self.name = name
        self.id = id
        self.contract = contract
        self.commission = commission

    def compute_pay(self) -> float:
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout
```
So what we've done now is defined the relationship here between the Employee the Contract and the Commission. And then we deal with how that interacts with each other in the compute pay method. And now what we can do is create specific contracts. So I could create an hourly contract. The ```HourlyContract```, that's going to be subclass of ```Contract```, obviously. I can make a ```SalariedContract``` as well. And that basically looks like this. And then finally, let's also create a ```FreelancerContract``` just for completeness. 

```py
class HourlyContract(Contract):
    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
        employer_cost: float = 1000,
    ) -> None:
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.employer_cost = employer_cost

    def get_payment(self):
        return self.pay_rate * self.hours_worked + self.employer_cost


class SalariedContract(Contract):
    def __init__(
        self,
        monthly_salary: float = 0,
        percentage: float = 1,
    ) -> None:
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def get_payment(self):
        return self.monthly_salary * self.percentage


class FreelancerContract(Contract):
    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
        vat_number: str = "",
    ) -> None:
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.vat_number = vat_number

    def get_payment(self):
        return self.pay_rate * self.hours_worked
```

Now this couple of things, we need to change in the ```main``` function, because now we obviously change the whole structure of the application. So we have commissions, contracts and employees. 

```py
def main():
    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=1002, contract=henry_contract)
    print(
        f"`{henry.name}` worked for `{henry_contract.hours_worked}` hours and earned `${henry.compute_pay()}`."
    )

    sarah_contract = SalariedContract(monthly_salary=5_000)
    sarah_commission = Commission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=2031, contract=sarah_contract, commission=sarah_commission
    )
    print(
        f"`{sarah.name}` landed `{sarah_commission.contracts_landed}` contracts and earned `${sarah.compute_pay()}`."
    )

if __name__ == "__main__":
    main()
```

Let's run the code again.
```
`Henry` worked for `100` hours and earned `$6000`.
`Sarah` landed `10` contracts and earned `$6000`.
```

### Improvement: Turn Commission into an abstract class
There is still a single commission class, but we could make this a little bit more generic by adding an actual abstract commission class. The following is the entire code.

```py
from abc import ABC, abstractmethod
from typing import Optional


class Commission(ABC):
    @abstractmethod
    def get_payment(self) -> float:
        pass


class ContractCommission(Commission):
    def __init__(
        self,
        commission: float = 100,
        contracts_landed: float = 0,
    ) -> None:
        self.commission = commission
        self.contracts_landed = contracts_landed

    def get_payment(self):
        return self.commission * self.contracts_landed


class Contract(ABC):
    @abstractmethod
    def get_payment(self) -> float:
        pass


class Employee:
    def __init__(
        self,
        name: str,
        id: int,
        contract: Contract,
        commission: Optional[Commission] = None,
    ) -> None:
        self.name = name
        self.id = id
        self.contract = contract
        self.commission = commission

    def compute_pay(self) -> float:
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout


class HourlyContract(Contract):
    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
        employer_cost: float = 1000,
    ) -> None:
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.employer_cost = employer_cost

    def get_payment(self):
        return self.pay_rate * self.hours_worked + self.employer_cost


class SalariedContract(Contract):
    def __init__(
        self,
        monthly_salary: float = 0,
        percentage: float = 1,
    ) -> None:
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def get_payment(self):
        return self.monthly_salary * self.percentage


class FreelancerContract(Contract):
    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
        vat_number: str = "",
    ) -> None:
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.vat_number = vat_number

    def get_payment(self):
        return self.pay_rate * self.hours_worked


def main():
    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=1002, contract=henry_contract)
    print(
        f"`{henry.name}` worked for `{henry_contract.hours_worked}` hours and earned `${henry.compute_pay()}`."
    )

    sarah_contract = SalariedContract(monthly_salary=5_000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=2031, contract=sarah_contract, commission=sarah_commission
    )
    print(
        f"`{sarah.name}` landed `{sarah_commission.contracts_landed}` contracts and earned `${sarah.compute_pay()}`."
    )


if __name__ == "__main__":
    main()
```

- Reference(s):
  - https://www.youtube.com/watch?v=0mcP8ZpUR38