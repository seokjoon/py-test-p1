with open('ds/array.py', 'r') as foos:
    print(foos.read())
    # print(foos.readlines())
    # for foo in foos:
    #    print(foo)

import urllib.request
with urllib.request.urlopen('https://memorobot.com') as bars:
    # print(bars.read())
    for bar in bars:
        bar = bar.strip()
        bar = bar.decode('utf-8')
        print(bar)

