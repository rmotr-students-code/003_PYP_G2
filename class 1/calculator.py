"""
Write a function that receives 2 numbers and performs simple calculations
(additions, subtractions, multiplications and divisions)
based on a string parameter.
Example:
    calculator(2, 3, 'add')       # Should return 5
    calculator(7, 3, 'subtract')  # Should return 4
    calculator(2, 7, 'multiply')  # Should return 14
    calculator(8, 4, 'divide')    # Should return 2
    calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""

from __future__ import division


def add_function(values):
    return sum(values)

def subtract_function(values):
    


def calculator(*args, **kwargs):
    operation = kwargs["operation"]
    values = kwargs["values"]
    return operation(values)   # add function

assert calculator(values=[1,2,3,4], operation=add_function()) == 10
assert calculator(values=[3,1], operation=subtract_function()) == 
#assert calculator(8, 2, 'add') == 10




