# Python3 的六个标准数据类型中：
# 不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）。

# 1.Number（数字）

print("-------------------------------------")
# Python3 支持 int、float、bool、complex（复数）
a1 = True
a2 = 12
a3 = 1.23
a4 = complex(1, 3)
print(type(a1), a1)  # ==><class 'bool'> True
print(type(a2), a2)  # ==><class 'int'> 12
print(type(a3), a3)  # ==><class 'float'> 1.23
print(type(a4), a4)  # ==><class 'complex'> (1+3j)


print("-------------------------------------")
# 关于Number的一些运算
# /运算结果为小数
print(4 / 2)  # ==>2.0
print(5 / 4)  # ==>1.25

# //运算结果舍弃余数
print(9.0 // 4)  # ==>2.0
print(9.2 // 4)  # ==>2.0
print(9 // 4)  # ==>2

# %运算保留余数
print(9.0 % 4)  # ==>1.0
print(9.2 % 4)  # ==>1.1999999999999993
print(9 % 4)  # ==>1

# **运算为幂运算
print(2 ** -1)  # ==>0.5

print("-------------------------------------")
# 关于Number的一些函数
# 绝对值abs(Number)
print(abs(-3))  # ==>3

# 向原点0取整
print(int(-2.3))  # ==>-2

# 四舍五入round(no_complex, 0)
print(round(3.1415, 3))  # ==>3.142


# 2.String（字符串）

print("-------------------------------------")

# 正索引
print("abcde"[0])  # ==>a

# 负索引，-n:倒数第n个元素
print("abcde"[-1])  # ==>e

# 切片str[m:n],m默认为0，n默认为len(str)
print("abcde"[1:3])  # ==>bc



