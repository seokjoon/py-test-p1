import bisect

data = [6, 50, 4, 30, 2, 10]
foo = []
for i in data:
    pos = bisect.bisect(foo, i)
    bisect.insort(foo, i)
    print(i, pos, foo)
