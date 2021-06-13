from itertools import *


# for i in chain([1, 2, 3], ['a', 'b', 'c']):
#     print(i, end=' ')
# print()


# def make_iterables_to_chain():
#     yield [1, 2, 3]
#     yield ['a', 'b', 'c']
#
#
# for i in chain.from_iterable(make_iterables_to_chain()):
#     print(i, end=' ')
# print()


# for i in zip([1, 2, 3], ['a', 'b', 'c']):
#     print(i)


r1 = range(3)
r2 = range(2)
print(list(zip(r1, r2)))
print(list(zip_longest(r1, r2)))
