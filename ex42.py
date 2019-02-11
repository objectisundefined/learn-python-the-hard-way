# Animal
#   Dog
#     name
#   Cat
#     name

class Animal(object):
  pass

class Dog(Animal):
  def __init__(self, name):
    self.name = name


class Cat(Animal):
  def __init__(self, name):
    self.name = name


# Person
#   name
#   pet None

class Person(object):
  def __init__(self, name):
    self.name = name
    self.pet = None


#   Employee
#   salary
#   super(Employee, self).__init__(name)

class Employee(Person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(name)
    self.salary = salary


# Fish
#   Salmon
#   Halibut

class Fish(object):
  pass


class Salmon(Fish):
  pass


class Halibut(Fish):
  pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

print(frank.name, frank.salary)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

# About class Name(object)
# In Python 3, you do not need to add the (object) after the name of the class, but the Python community believes in
# “explicit is better than implicit,” so I and other Python experts have decided to include
# it. You may run into code that does not have (object) after simple classes, and those classes are
# perfectly fine and will work with classes you create that do have (object). At this point it is simply
# extra documentation and has no impact on how your classes work.

# What does super(Employee, self).__init__(name) do? That’s how you can run the
# __init__ method of a parent class reliably.

# https://docs.python.org/3/library/functions.html#super

# super([type[, object-or-type]])
#   Return a proxy object that delegates method calls to a parent or sibling class of type.
#   This is useful for accessing inherited methods that have been overridden in a class.
#   The search order is same as that used by getattr() except that the type itself is skipped.

# class C(B):
#     def method(self, arg):
#         super().method(arg)    # This does the same thing as:
#                                # super(C, self).method(arg)
