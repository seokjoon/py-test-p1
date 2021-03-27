import collections

foo = {'foo': 1, 'bar': 2}
bar = {'fee': 3, 'bee': 4}

"""
outs = collections.ChainMap(foo, bar)
print(outs)
print(list(outs.keys()))
print(list(outs.values()))
for k, v in outs.items():
    print(k, v)
"""

outs = collections.Counter()
outs.update(foo)
outs.update(bar)
outs.update(foo)
print(outs)
for n in 'fee':
    print(outs[n])
