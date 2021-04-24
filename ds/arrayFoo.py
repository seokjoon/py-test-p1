import array

# foo = b'foo'
# bar = array.array('b', foo)
# print(bar)

# foo = array.array('i', range(3))
# print(foo)
# foo.extend(range(3))
# print(foo)
# print(foo[2:5])
# print(list(enumerate(foo)))

import binascii
import tempfile
foo = array.array('i', range(6))
print(binascii.hexlify(foo.tobytes()))
bee = array.array('i')
bee.frombytes(foo.tobytes())
print(bee)
bar = tempfile.NamedTemporaryFile()
foo.tofile(bar.file)
bar.flush()
with open(bar.name, 'rb') as input:
    raw = input.read()
    print(raw)
    print(binascii.hexlify(raw))
    input.seek(0)
    fee = array.array('i')
    fee.fromfile(input, len(foo))
    print(fee)
