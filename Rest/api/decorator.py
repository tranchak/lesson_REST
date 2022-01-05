from datetime import datetime


def decorator(fn):
    def wrapper():
        start = datetime.now()
        results = fn()
        print(datetime.now() - start)
        return results

    return wrapper


@decorator
def one():
    # start = datetime.now()
    l = []
    for i in range(5):
        l.append(i)
    # print(datetime.now() - start)
    return l


@decorator
def two():
    # start = datetime.now()
    l = [i for i in range(5)]
    # print(datetime.now() - start)
    return l


print(two())
# d=decorator(two)
# print(d())

# a = one()
# b = two()
# print(one())
# print(two())
# print(a)
# print(b)
