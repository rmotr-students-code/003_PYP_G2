
"""
Implement a @small_arguments decorator for the "sum(a, b)" function, 
that raises ValueError if any of given arguments are greater than 10.

Examples:
    sum(2, 4)  # 6
    sum(11, 4)  # ValueError
"""


def small_arguments(original_function):
    def func(a, b):
        if max(a,b) > 10:
            raise ValueError
        else:
            return original_function(a,b)
    return func

@small_arguments
def sum(a, b):
    return a + b
