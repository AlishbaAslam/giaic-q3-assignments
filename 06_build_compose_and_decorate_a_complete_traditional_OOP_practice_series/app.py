# 1. Using self

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

s1 = Student("Ali", 90)
s1.display()

# 2. Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects: {cls.count}")

c1 = Counter()
c2 = Counter()
Counter.show_count()

# 3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

my_car = Car("Toyota")
print(my_car.brand)
my_car.start()

# 4. Class Variables and Class Methods

class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()

print(b1.bank_name)
Bank.change_bank_name("New Bank")
print(b2.bank_name)

# Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))

# Constructors and Destructors

class Logger:
    def __init__(self):
        print("Logger created.")

    def __del__(self):
        print("Logger destroyed.")

log = Logger()
del log  # Optional explicit delete

# Access Modifiers

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # public
        self._salary = salary    # protected
        self.__ssn = ssn         # private

emp = Employee("Ali", 50000, "123-45-6789")
print(emp.name)          # Accessible
print(emp._salary)       # Accessible but not recommended
# print(emp.__ssn)       # Error
print(emp._Employee__ssn)  # Correct way to access private var

# The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Sarah", "Math")
print(t.name, "-", t.subject)

# Abstract Classes and Methods

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

r = Rectangle(5, 3)
print(r.area())

# Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

d = Dog("Max", "Labrador")
d.bark()

# Class Methods

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))

# 13. Composition

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_car()

# 14. Aggregation

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

e = Employee("Ali")
d = Department(e)
print(d.employee.name)

# 15. MRO and Diamond Inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # MRO: D -> B -> C -> A

# 16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators

def add_greeting(cls):
    class NewClass(cls):
        def greet(self):
            return "Hello from Decorator!"
    return NewClass

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())

# 18. Property Decorators

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print(p.price)
p.price = 150
print(p.price)
del p.price

# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(5)
print(callable(m))       # True
print(m(10))             # 50

# 20. Custom Exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Age is valid.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)

# 21. Custom Iterable Class

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)
