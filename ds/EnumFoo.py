import enum


class EnumFoo(enum.Enum):

    foo = 1
    bar = 2


print(EnumFoo.foo, EnumFoo.foo.name, EnumFoo.foo.value)
for n in EnumFoo:
    print(n.name, n.value)
print(EnumFoo.foo == EnumFoo.bar, EnumFoo.foo is EnumFoo.bar)


