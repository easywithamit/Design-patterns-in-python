#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Amit Kumar
@mail: haywithamit.com

Template Method Design Pattern::
We have a template method which performs all the steps in case class(Abstract)
However the steps are not implemented here but in the subclasses which inherit
it.Since python does not provide facility to stop a method from being overriden.
It can be implemented explicity by creating another metaclass.
"""

from abc import ABCMeta,abstractmethod


class Lunch:
    __metaclass__ = ABCMeta

    def prepare_lunch(self):
        self.prepare_ingredients()
        self.cook()
        self.eat()

    @abstractmethod
    def prepare_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def eat(self):
        pass


# Overriding the steps of the parent class and not the template method


class Dominos(Lunch):
    def prepare_ingredients(self):
        print("Prepare pizza crust, seasons and all topping")

    def cook(self):
        print("Make the pizza")

    def eat(self):
        print("Eat your pizza before it becomes cold!")


class KFC(Lunch):
    def prepare_ingredients(self):
        print("Get the chiken and spices")

    def cook(self):
        print("Grill it hot!")

    def eat(self):
        print("Yummy")


if __name__=='__main__':
    l = Dominos()
    l.prepare_lunch()
