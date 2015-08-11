"""
def a_function(elem):
    return elem ** 2

print "Map"
print map(a_function, [1, 2, 3, 4])

print "Filter"
print filter(lambda x: x % 2 == 0, [1, 2, 3, 4])


print "Reduce"
print reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 5)
"""


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum([e ** 2 for e in a_list if e < 5])

reduce(lambda acc, x: acc + x, map(lambda x: x ** 2, (filter(lambda x: x < 5, a_list))))
