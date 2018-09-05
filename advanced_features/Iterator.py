from collections import Iterable
from collections import Iterator

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.可迭代对象（Iterable）                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 含有 __iter__() 方法或 __getitem__() 方法的对象称之为可迭代对象。

# # 用Python 内置的 hasattr()来判断是不是可迭代对象

print(hasattr((), '__iter__'))  # ==>True
print(hasattr([], '__iter__'))  # ==>True
print(hasattr({}, '__iter__'))  # ==>True
print(hasattr(123, '__iter__'))  # ==>False
print(hasattr('abc', '__iter__'))  # ==>True
print(hasattr('abc', '__getitem__'))  # ==>True

# # 使用isinstance()来判断
print(isinstance((), Iterable))  # ==>True<==元组
print(isinstance([], Iterable))  # ==>True<==列表
print(isinstance({}, Iterable))  # ==>True<==字典
print(isinstance('abc', Iterable))  # ==>True<==字符串
print(isinstance(100, Iterable))  # ==>False<==数字

# 可迭代对象都能使用for循环迭代
for x in "abc":
    print(x)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   2.迭代器（Iterator）                    #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 迭代器是指遵循迭代器协议（iterator protocol）的对象
# # 迭代器协议是指要实现对象的 __iter()__ 和 __next__() 方法(Python2是next方法)

# # 使用isinstance()来判断
print(isinstance((), Iterator))  # ==>False
print(isinstance(iter(()), Iterator))  # ==>True<==iter() 函数获得它们的迭代器对象
print(isinstance([], Iterator))  # ==>False
print(isinstance(iter([]), Iterator))  # ==>True
print(isinstance({}, Iterator))  # ==>False
print(isinstance(iter({}), Iterator))  # ==>True
print(isinstance('', Iterator))  # ==>False
print(isinstance(iter(''), Iterator))  # ==>True
print(isinstance(123, Iterator))  # ==>False


for x in [1, 2, 3]:
    print(x)

# 等价于

it = iter([1, 2, 3])  # 获得 Iterator 对象
while True:  # 循环
    try:
        x = next(it)  # 获得下一个值
        print(x)
    except StopIteration:
        break  # 没有后续元素，退出循环
