# single_responsibility.py
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

class SalaryCalculator:
    @staticmethod
    def calculate_payroll(employees):
        total = 0
        for employee in employees:
            total += employee.salary
        return total

# open_closed.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_total_area(self, shapes):
        return sum(shape.area() for shape in shapes)

# dependency_inversion.py
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class Order:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def checkout(self, amount):
        self.processor.process_payment(amount)

# composition_over_inheritance.py
class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels rotating")

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        self.engine.start()
        self.wheels.rotate()
        print("Car is moving")

# Uso
if __name__ == "__main__":
    # Single Responsibility Principle
    emp1 = Employee("John Doe", "Developer", 5000)
    emp2 = Employee("Jane Smith", "Designer", 4500)
    db = EmployeeDatabase()
    db.add_employee(emp1)
    db.add_employee(emp2)
    calculator = SalaryCalculator()
    total_payroll = calculator.calculate_payroll(db.employees)
    print(f"Total payroll: ${total_payroll}")

    # Open-Closed Principle
    rect = Rectangle(5, 10)
    circle = Circle(7)
    calculator = AreaCalculator()
    total_area = calculator.calculate_total_area([rect, circle])
    print(f"Total area: {total_area}")

    # Dependency Inversion Principle
    credit_order = Order(CreditCardProcessor())
    credit_order.checkout(100)

    paypal_order = Order(PayPalProcessor())
    paypal_order.checkout(150)

    # Composition over Inheritance
    car = Car()
    car.drive()
