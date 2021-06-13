import functools


def foo(a, b=0):
    print(' called foo with: ', a, b)


def show_details(name, f, is_partial=False):
    print('{}', format(name))
    print(' object: ', f)
    if not is_partial:
        print(' __name__', f.__name__)
    else:
        print(' func: ', f.func)
        print(' args: ', f.args)
        print(' keywords: ', f.keywords)
    return


show_details('foo', foo)
foo('a', 2)
print()

p1 = functools.partial(foo, 'a', b=3)
show_details('foo with param', p1, True)




