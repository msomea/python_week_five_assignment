OOP Assignment – Python

This project demonstrates key concepts of Object-Oriented Programming (OOP) using Python, including Classes & Objects, Constructors, Inheritance, Polymorphism, and Encapsulation

Assignment 1: Designing Class
Description
A Smartphone class was designed to represent a real-world smartphone with attributes and methods.
It inherits from a base class Device to demonstrate inheritance.
Features
Attributes: brand, model, storage, battery
Methods:
call(number) – Simulates making a call
charge(percent) – Charges the battery
Constructor: Initializes each smartphone with unique values
Inheritance: Smartphone extends Device

Example Usage
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 50)
print(phone1.call("+25523456789"))
print(phone1.charge(15))


Asignment 2: Polymorphism
Description
A set of classes representing different vehicles demonstrates polymorphism using a common method move().
Classes
Car – move() → "Driving 🚗"
Plane – move() → "Flying ✈️"
Boat – move() → "Sailing ⛵"

Example Usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())

