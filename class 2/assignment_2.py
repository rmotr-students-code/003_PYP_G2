"""
Write a function that receives a list of numbers
and a list of terms and returns only the elements that are divisible
by all of those terms. You must use two nested list comprehensions to solve it.

Example:
    divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])  # [12, 6]

"""


def divisible_numbers(a_list, a_list_of_terms):
    """
    new_list = []
    for number in a_list:
        if is_divisible(number, a_list_of_terms):
            new_list.append(number)
    return new_list
    """
    return [n for n in a_list if all([n % term==0 for term in a_list_of_terms])]
    



assert set(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3]))  == set([6, 12])
assert divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4])  == [12]