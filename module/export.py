def bar(val: int) -> int:
    """
    >>> bar(2)
    4
    """
    return val * 2


def boo() -> None:
    print(input('input: '))


def foo(val: str) -> None:
    print(__name__ + val)


if __name__ == '__main__':
    print(__name__, 'statement', foo('1'), bar(2))
    boo()
    import doctest
    print(doctest.testmod())
