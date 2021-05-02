import copy
import functools


@functools.total_ordering
class CopyFoo:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


foo = CopyFoo('Foo')
fee = [foo]
bar = copy.copy(fee)
print(fee)
print(bar)
print(fee is bar)
print(fee == bar)
print(fee[0] is bar[0])
print(fee[0] == bar[0])
print()


foo = CopyFoo('Foo')
fee = [foo]
bar = copy.deepcopy(fee)
print(fee)
print(bar)
print(fee is bar)
print(fee == bar)
print(fee[0] is bar[0])
print(fee[0] == bar[0])