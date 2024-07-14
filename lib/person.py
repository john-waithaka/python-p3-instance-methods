#!/usr/bin/env python3

# class Person:
#     # Class body goes here

#     #Instance method definition
#     pass

# Complete the following tasks to get the rest of the tests passing:

# Add an instance method talk() to your Person class that will print "Hello World!"
# Add an instance method walk() to your Person class that will print "The person is walking."


class Person:
    def talk(self):
        print("Hello World!")
    
    def walk(self):
        print("The person is walking.")

person1 = Person()

person1.talk()
person1.walk()


