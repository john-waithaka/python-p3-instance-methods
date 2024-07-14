#!/usr/bin/env python3

# class Dog:
#     # Class body goes here

#     #Instance method definition
#     pass

# Complete the following tasks to get the rest of the tests passing:

# Add an instance method sit() to your Dog class that will print "The dog is sitting."
# Define a Person class in lib/person.py


class Dog:
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")


dog1 = Dog()

dog1.bark()

dog1.sit()