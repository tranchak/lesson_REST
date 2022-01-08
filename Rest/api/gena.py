import time

import request


for c in range(1,5):
    time.sleep(0.5)
    print(c)

def fn():
    for i in range(0,20):
        yield i

def fn_2():
    yield from fn()
    yield from ['a','b','c']

d=fn_2()
for i in d:
    print(i)