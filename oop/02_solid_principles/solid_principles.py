from abc import ABC, abstractmethod


class Order:
    items: list[str] = []
    quantities: list[int] = []
    prices: list[float] = []
    status = "open"

    def add_item(self, item_name: str, item_quantity: int, item_price: float):
        self.items.append(item_name)
        self.quantities.append(item_quantity)
        self.prices.append(item_price)

    def total_price(self) -> float:
        return sum(
            [
                self.quantities[index] * self.prices[index]
                for index in range(len(self.items))
            ]
        )


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuthorizer(Authorizer):
    SMS_CODE = 999

    def __init__(self) -> None:
        self.is_valid = False

    def verify(self, code: int):
        if code == self.SMS_CODE:
            self.is_valid = True

    def is_authorized(self):
        return self.is_valid


class NotARobot(Authorizer):
    HEX_CODE = "0x3e7"

    def __init__(self) -> None:
        self.is_valid = False

    def verify(self, image_code: int):
        if hex(image_code) == self.HEX_CODE:
            self.is_valid = True

    def is_authorized(self):
        return self.is_valid


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int, auth: Authorizer) -> None:
        self.security_code = security_code
        self.authorizer = auth

    def pay(self, order: Order):
        if self.authorizer.is_authorized() is True:
            print("Processing debit card payment...")
            print(f"Verifying security code: {self.security_code}")
            order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int, auth: Authorizer) -> None:
        self.security_code = security_code
        self.authorizer = auth

    def pay(self, order: Order):
        if self.authorizer.is_authorized() is True:
            print("Processing credit card payment...")
            print(f"Verifying security code: {self.security_code}")
            order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address: str) -> None:
        self.email_address = email_address

    def pay(self, order: Order):
        print("Processing paypal payment...")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


def main():
    order = Order()
    order.add_item("Mangoes", 5, 5.0)
    order.add_item("Bananas", 12, 2.0)
    order.add_item("Mangoes", 18, 20.0)
    cost = order.total_price()
    print(f"Your total cost is: {cost}")
    print()
    user_input = int(
        input(
            "Which payment method you want to choose? We offer [1]debit / [2]credit / [3]Paypal. "
        )
    )

    if user_input == 1:
        # Verifying the SMS
        sms = SMSAuthorizer()
        sms_code = int(input("We have send you a code on +....39: "))
        sms.verify(sms_code)
        # Proceed to Payment
        security_code = int(input("Please provide security code: "))
        payment_processor = DebitPaymentProcessor(security_code, sms)
        payment_processor.pay(order)

    elif user_input == 2:
        # Verifying the SMS
        sms = SMSAuthorizer()
        sms_code = int(input("We have send you a code on +....39: "))
        sms.verify(sms_code)
        # Proceed to Payment
        security_code = int(input("Please provide security code: "))
        payment_processor = CreditPaymentProcessor(security_code, sms)
        payment_processor.pay(order)

    elif user_input == 3:
        # Verifying Not a Robot
        robot = NotARobot()
        robot_code = int(input("Please verify you are a human: "))
        robot.verify(robot_code)
        # Proceed to Payment
        email_address = input("Please provide email address: ")
        payment_processor = PaypalPaymentProcessor(email_address)
        payment_processor.pay(order)

    else:
        raise Exception("We donot support anyother payment methods.")

    print()
    print(f"Your payment status is: {order.status}")


if __name__ == "__main__":
    main()
