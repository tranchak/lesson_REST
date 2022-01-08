'''генератор - функция которая возвращает объект итератор
элементы которого можно перебирать один раз

Итератор -

'''

# генератор реализованный на классе
class Range_my:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        while self.start <= self.end:
            yield self.start
            self.start += self.step

    def __iter__(self):
        return self.__next__()


a = Range_my(0, 20, 2)
c = a.__iter__()
print(c.__next__())
print(c.__next__())
for i in c:
    print(i)


print(type(c))
# print(next(c))
# print(next(c))
# print(next(c))


# # def fn():
# #     l=10
# #
# #     yield l
# #     print(l)
# #
# # s=fn()
# # print(s)
# # print(s.__next__())
# # print(s.__iter__())
#
#
# # # генератор списка
# # a = [i for i in range(6)]
# # print(a)
#
# # # выражение генератор
# # b = (i for i in range(6))
# # print(b) # выводит объект генератора
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(dir(b))
# #
# # s=[1,2,3,4,5,6,7,8]
# # print(type(s))
# # f=iter(s) # это итератор. Он имеет функцию next
# # print(type(f))
# # print(dir(f))
# # print(next(f))
# # print(next(f))
# # print(next(f))

# c=list(range(10000000))
# print(c)
# print(c.__sizeof__())
# d = (i for i in range(10))
# print(d)
# print(d.__sizeof__())
#
# f=iter(range(5))
# for i in f:
#  print(i)
# for i in f:
#  print(i)

#
# s='1 2 3'
# print(dir(s))
# for i in s:
#  print(i)
# for i in s.__iter__():
#  print(i)

#
# def fn():
#     l=10
#     for i in [1,2,3,4,5]:
#         yield i
#         print(l)
#         l=10*i
#
# s=fn()
# print(type(s))
# print(next(s))
# print(next(s))
# print(next(s))
#
