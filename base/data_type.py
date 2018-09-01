# Python3 的六个标准数据类型中：
# 不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）。改变值时重新分配内存
# 可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）。


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                       1.Number（数字）                   #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# Python3 支持 int、float、bool、complex（复数）
a1 = True
a2 = 12
a3 = 1.23
a4 = complex(1, 3)
print(type(a1), a1)  # ==><class 'bool'> True
print(type(a2), a2)  # ==><class 'int'> 12
print(type(a3), a3)  # ==><class 'float'> 1.23
print(type(a4), a4)  # ==><class 'complex'> (1+3j)

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

# 关于Number的一些函数
# 绝对值abs(Number)
print(abs(-3))  # ==>3

# 向原点0取整
print(int(-2.3))  # ==>-2

# 四舍五入round(no_complex, 0)
print(round(3.1415, 3))  # ==>3.142

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   2.String（字符串）                     #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 行延续
str1 = "ab" + \
       "cde"
# 一对封闭括号中的代码都可多行显示
str2 = ("ab" +
        "cde")

# 正索引
print("abcde"[0])  # ==>a

# 负索引，-n:倒数第n个元素
print("abcde"[-1])  # ==>e

# 切片str[m:n],m默认为0，n默认为len(str)
print("abcde"[1:3])  # ==>bc
print("abcde"[1:])  # ==>bcde
print("abcde"[:2])  # ==>ab

# 字符串的一些运算
print("hello" * 3)  # ==>hellohellohello
print("hello" + " world")  # ==>hello world

# 字符串的一些函数
# 大小写转换
print("Python".upper())  # ==>PYTHON
print("Python".lower())  # ==>python
print("hello world".capitalize())  # ==>Hello world
print("hello world".title())  # ==>Hello World

# 非重叠字符串的数量
print("ablllabllab".count("ll"))  # ==>2

# 字符串查找
print("hihihi".find("hi"))  # ==>0
print("hihihi".rfind("hi"))  # ==>4

# 字符串替换所有
print("To a To b".replace('To', 'to'))  # ==>to a to b

# 首尾去除,默认空格
print("first-first-end".strip('find'))  # ==>rst-first-e
print("first-first-end".strip('first-'))  # ==>end
print("first-end-end".rstrip('-end'))  # ==>first

# 用于输出的对齐,默认填充空格
print("hello".ljust(9, '-') + "hello".center(9, '+') + "hello".rjust(9, '-'))  # ==>hello----++hello++----hello

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                       3.List（列表）                     #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 赋值
l1 = ['1', '2', '3', '4', '1']
l2 = ['1', '2',
      '3']
l2[0] = '2'

# 索引,通用序列操作
print(l1[-2])  # ==>4

# 切片[左索引:右索引:步长],通用序列操作
print(l1[0:5])  # ==>['1', '2', '3', '4', '1']
print(l1[0:5:2])  # ==>['1', '3', '1']
print(l1[5::-1])  # ==>['1', '4', '3', '2', '1']

# 加法和乘法类似字符串,通用序列操作

# 检验值是否存在序列中,通用序列操作
print(2 in [1, 2, 3, 4])  # ==>True
print('bc' in 'abcde')  # ==>True

l1.count('1')  # 统计某个元素出现的次数
l1.index('1')  # 找出某个元素的第一次出现的位置
l1.reverse()  # 将元素进行反转
l1.sort(reverse=True)  # 对列表进行反向排序,列表被改变,返回值是空
l1.append('5')  # 向末尾添加一个元素
l1.insert(3, '6')  # 向指定索引位置添加一个元素
l1.extend(['1', '2'])  # 向末尾添加，等同于 li + ['1','2']
l1.pop(3)  # 删除指定索引位置的一个元素，默认末尾
l1.remove('1')  # 移除列表中的第一个匹配元素
l1.clear()  # 清空所有元素

# split和join
print("1,2,3,4,5".split(','))  # ==>['1', '2', '3', '4', '5']
# join参数中的元素不能为数字
print(",".join(['1', '2', '3', '4', '5']))  # ==>1,2,3,4,5

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                       4.Tuple（元组）                    #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 单值元组
tt = ('a',)

# 多值元组
t = ('a', 'b', 'c')
print(t)  # ==>('a', 'b', 'c')
(x, y, z) = t
print(x + y + z)  # ==>abc

# 元组也是一种序列，因此也可以对它进行索引、分片等。
# 由于它是不可变的，因此就没有类似列表的 append, extend, sort 等方法。


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   5.Dictionary（字典）                   #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

d0 = {}
d1 = {'name': 'xiaoming', 'age': 20}
d1['age'] = 10
d2 = dict(name='xiaoming', age=20)
item = [('name', 'xiaoming'), ('age', 20)]
d3 = dict(item)

# 判断键是否不在字典里面
print('name' not in d1)  # ==>False

# 要删除字典的某一项
for k in list(d2.keys()):
    if k == 'name':
        del d2[k]

# 常用方法
d0.clear()
d0 = d1.copy()  # 浅复制,对可变对象的修改保持同步，对不可变对象的修改保持独立。
d0.get('phone')  # d['phone']不存在会抛异常，而get()会返回None
d0.get('phone', 'age')  # 第一个不存在则访问默认值age
d0.setdefault('age', '18')  # 设置默认值，如果存在，则不修改
d0.update(d2)  # 将一个字典添加到原字典,存在相同的键则会进行覆盖
print(d3.items())  # ==>dict_items([('name', 'xiaoming'), ('age', 20)])
print(list(d3.items()))  # ==>[('name', 'xiaoming'), ('age', 20)]
print(d3.keys())  # ==>dict_keys(['name', 'age'])
print(list(d3.keys()))  # ==>['name', 'age']
print(d3.values())  # ==>dict_values(['xiaoming', 20])
print(list(d3.values()))  # ==>['xiaoming', 20]
d3.pop('name')  # 移除指定key的键值对，不存则在抛异常
d3.popitem()  # 随机移除键值对

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   6.Set（集合）                          #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

s1 = {'a', 'b', 'c', 'd', 'a'}
print(s1)  # ==>{'c', 'b', 'a', 'd'}
s2 = set('hello')
print(s2)  # ==>{'h', 'e', 'l', 'o'}
print(set([1, 2, 3]))  # ==>{1, 2, 3}

# 常用方法
s1.add('ff')
s1.remove('ff')  # 删除不存在的元素，会抛出异常

# 交集/并集/差集
s1 & s2  # 交集
s1 | s2  # 并集
s1 - s2  # 差集
s2.issubset(s1)    # s2 是否是 s1 的子集
s1.issuperset(s2)  # s1 是否是 s2 的超集
