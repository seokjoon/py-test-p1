import gc
import weakref


class WeakrefFoo:
    def __del__(self):
        print(self)


def callback(ref):
    print(ref)


foo = WeakrefFoo()
# bar = weakref.ref(foo)
bar = weakref.ref(foo, callback)

print(foo)
print(bar)
del foo
print(bar)
print()


def on_finalize(*args):
    print(args)


foo = WeakrefFoo
bar = weakref.finalize(foo, on_finalize, 'BAR')
print(bar)
del foo
print(bar)
print()


foo = WeakrefFoo
foo_id = id(foo)
bar = weakref.finalize(foo, on_finalize, foo)
bar.atexit = False
print(bar)
del foo
print(bar)
for o in gc.get_objects():
    if id(o) == foo_id:
        print('found uncollected object in gc')
print()


class WeakrefBar:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self)


foo = WeakrefBar('FOO')
bar = weakref.proxy(foo)
print(foo.name)
print(bar.name)
del foo
print(bar.name)


