# Iterable = an object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop
#            list(); tuple[]; set{} - are iterable, but set{} cannot be reversed
#            strings are also iterable, each element will be separate
#            dictionary{key: value} - normally return only keys but with .values or .items
#                                     you can get values or both

# Membership operators = used to test whether a value or  variable is found in a sequence
#                        //string, list, tuple, set or dictionary//
#                        1. in
#                        2. not in

# List comprehension = a concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression FOR value IN iterable IF condition]

# Module = a file containing code you want to  include to your program
#          use "import" to  include a module //built-in or your own//
#          useful to break up large program reusable separate files

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# object = a "bundle" of related attributes (variables) and methods (functions)
#          You need a "class" to create many objects
# class = 'blueprint' used to design the structure and layout of an object

# class variables = shared among all instances of a class
#                   defined OUTSIDE the constructor
#                   allow to share data among all objects created from that class

# Inheritance = allows a class to inherit attributes  and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)

# multiple inheritance = inherit from more than one parent
#                        C(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# super() = function used in a child class to call methods from a parent class (superclass).
#           allows to extend the functionality of the inherited methods

# Polymorphism = Many forms
#                1. Inheritance = an object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

# Static method = a method that belongs to a class rather than any object from that class //instance//
#                 usually used for general  utility functions
# Instance method = best for operations on instances of the class //object//
# Static method = best for utility functions that do not need access to class data

# Class methods = allow operations related to the class itself
#                 take (cls) as the first parameter, which represents the class itself.

# Magic methods = Dunder methods //__// __init__, __str__, __eq__
#                 automatically called by many of Python built-in operations
#                 allow developers to define or customize the behavior of objects

# @property = decorator used to define a method as a property //can be accessed like an attribute//
#             add additional logic when read, write or delete attributes
#             gives 'getter', 'setter' and 'deleter' method

# Decorator = function that extends the behavior of another function
#             without modifying the base function
#             pass the base function as an argument to the decorator

# exception = an event that interrupts the flow of the program
#             //ZeroDivisionError, TypeError, ValueError//
#             try ; except ; finally

# File detection = to be able to work with system we have to //import os// <- operating file
#                  based on file extension we work we have to import different modules
#                  import json | import csv

# File writing = that can be done with //with// funktion.
#                It will open file to work with it and close when we are done
#                with open(file=,mode=) as file 
#                "w" - write a file; 
#                "x" - write file, that not exist; 
#                "r" - read file; 
#                "a" - append a file  
