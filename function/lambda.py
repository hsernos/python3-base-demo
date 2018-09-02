# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   1.高级函数                             #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


def double(x):
    return 2 * x


def triple(x):
    return 3 * x


def square(x):
    return x * x


# 遍历修改数组案例,数据数组和函数数组皆可以
print([double(x) for x in [0, 1, 2, 3]])  # ==>[0, 2, 4, 6]
print([f(2) for f in [double, triple, square]])  # ==>[4, 6, 4]


# 高级函数是能将函数做参数的函数
def func(g, arr):
    return [g(x) for x in arr]


print(func(double, [0, 1, 2, 3]))  # ==>[0, 2, 4, 6]
print(func(triple, [0, 1, 2, 3]))  # ==>[0, 3, 6, 9]
print(func(square, [0, 1, 2, 3]))  # ==>[0, 1, 4, 9]

# map(function, sequence)
# 对 sequence 中的 item 依次执行 function(item)
# 结果组成一个 List迭代器返回，python2返回list，和上面func函数差不多
print(list(map(double, [0, 1, 2, 3])))  # ==>[0, 2, 4, 6]

# filter(function, sequnce)
# 将 function 依次作用于 sequnce 的每个 item，
# 即 function(item)，将返回值为 True 的 item 组成一个 List/String/Tuple
# (取决于 sequnce 的类型，python3 统一返回迭代器) 返回
def is_great_then_3(x):
    return x > 3

print(list(filter(is_great_then_3, [1, 2, 3, 4, 5, 6, 7])))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   2.lambda表达式                         #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 定义：lambda 参数: 表达式
print((lambda x: 2 * x)(2))  # ==>4
f = lambda x: 2 * x
print(f(2))  # ==>4
print(type(f))  # ==><class 'function'>

# lambda函数一般适用于创建一些临时性的
print([(lambda i: 2 * i)(x) for x in [0, 1, 2, 3]])  # ==>[0, 2, 4, 6]
print(list(map(lambda x: x * x, [1, 2, 3, 4])))  # ==>[1, 4, 9, 16]

