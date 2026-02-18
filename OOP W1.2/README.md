# **OOP W1.2 - The Four Pillars**

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which contain data (attributes) and behavior (methods). It helps organize code in a reusable and structured way. 

[Sources](https://www.geeksforgeeks.org/python/python-oops-concepts/#:~:text=Four%20Pillars%20of%20OOP%20in%20Python)

Embed code with:

```py
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

cat = Animal("Whiskers")
cat.speak()
```

To understand OOP, one must be familar with the Four Basic Pillars that constitute it. 


1. Inheritance
2. Abstraction
3. Polymorphism 
4. Encapsulation


## Inheritance

Inheritance allows a class to inherit attributes and methods from another class. It promotes code reuse.

```py
#INHERITANCE
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()
```
> [!NOTE] 
> Remember to avoid multiple inheritance, as it becomes hard to maintain with little to no benefits

---

## Abstraction

Abstraction hides implementation details and shows only essential features of an object.



```py
#ABSTRACTION
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

circle = Circle()
print(circle.area())
```
> [!NOTE]
> After defining the abstract class, never attempt to inherit the object directly. Instead, inherit the abstract class first. 
---

## Polymorphism

Polymorphism allows methods to do different things based on the object calling them.

```py
#POLYMORPHISM
class Bird:
    def speak(self):
        print("Chirp")

class Dog:
    def speak(self):
        print("Bark")

for animal in (Bird(), Dog()):
    animal.speak()
```

---

## Encapsulation

Encapsulation restricts direct access to some components of an object to protect the integrity of the data.

```py
#Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
```

## License

The code is free to use and modify for your own projects.
