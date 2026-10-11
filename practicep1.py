# OOP programming paradigm
class BankAccount:
    # Constructor for the attributes. Dunder method is a special method
    def __init__(self, acc, id, balance=0):
        # First argument of any method in a class is always self. It is a reference to the current instance of the class.
        # It is used to access variables that belong to the class.
        self.acc = acc
        self.id = id
        self.balance = balance

    def deposit(self, amount):
          self.balance = self.balance + amount

    def withdraw(self, amount):
          self.balance = self.balance - amount

    def checbal(self):
          return self.balance
    # Attributes are variables that belong to a class. They are used to store data about the object.
    # Methods are functions that belong to a class. They are used to define the behavior of the object.
    John = BankAccount(85756, 1000)
    Brian = BankAccount(67890, 500)
    ...
    # dot attribute notation is used to access the attributes and methods of the class.
    print(John.acc)
    print(John.balance)
    print(John.deposit(300))
    print(John.balance)
    print(John.withdraw(200))
    print(John.balance)


"""1. Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties and behaviors
from another class.
The class that is inherited from is called the parent class or superclass,
and the class that inherits from it is called the child class or subclass.  Inheritance allows for code reuse and the
creation of a hierarchical relationship between classes.
 In Python, inheritance is implemented by defining a new class that takes the parent class as an argument
in its definition."""
"""2. Encapsulation is the process of hiding the internal details of an object and only exposing the necessary parts.
  It is a way to protect the data and methods of an object from being accessed or modified by external code.
In Python, encapsulation is achieved by using private attributes and methods, which are denoted by a leading
 underscore (_). Private attributes and methods can only be accessed within the class and cannot be accessed from
 outside the class."""

 class Vehicle:
    def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

    def forward(self, speed):
         print(f"car moved at {speed}km/hr")
mycar = Vehicle("Toyota", "Camry", 2020)
mycar.forward(60)
# Inheritance


class Marcedes(Vehicle):
      # can access the attributes and methods of the parent class Vehicle
      def __init__(self, make, model, year):
           # super() function is used to call the constructor of the parent class.
           #  It allows us to access the attributes and methods of the parent class.
           super().__init__(make, model, year)

      def __forward(self, speed):
           print(_f"Marcedes moved at {speed}km/hr")


"""2. Abstraction is the process of hiding the implementation details and showing only the functionality to the user.
Abstract class is a class that cannot be instantiated. It is used as a blueprint for other classes.
An abstract class can have abstract methods, which are methods that are declared but do not have an implementation.
Abstract classes are used to define a common interface for a group of related classes.
"""

"""3. Polymorphism is the ability of an object to take on many forms.
It allows objects of different classes to be treated as objects of a common superclass.
In Python, polymorphism is achieved through method overriding and method overloading.
Method overriding allows a subclass to provide a specific implementation of a method that is already defined in
its superclass. Method overloading allows a class to have multiple methods with the same name but different parameters."""

    def __init__(self, account_number, account_holder, balance=0):
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited: {amount}. New balance: {self.balance}")
            else:
                print("Deposit amount must be positive.")
    
        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds or invalid withdrawal amount.")
    
        def get_balance(self):
            return self.balance