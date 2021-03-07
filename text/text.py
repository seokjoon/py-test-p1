"""
import textwrap
print(textwrap.fill('  fooooo fooooo foo foo foo foo', width=10))
print(textwrap.shorten('foo  bar bar foo foo bar bar foo', 10, placeholder=' ...'))
"""

"""
import re
print(re.search('fo', 'foooo').end())
print(re.findall('fo', 'fofofofo'))
for bar in re.finditer('fo', 'fofofofo'):
    print(bar.start())
"""

import difflib
print('foo \n bar'.splitlines())
print('\n'.join(difflib.Differ().compare('foo', 'bar')))
print('===')
print('\n'.join(difflib.unified_diff('foo', 'bar', lineterm='')))
