# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   1.关系及逻辑运算                       #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 关系运算符
print("abc" < "abcb")  # ==>True
print("abc" > "abcb")  # ==>False
print("abc" == "abcb")  # ==>False
print("abc" <= "abcb")  # ==>True
print("abc" >= "abcb")  # ==>False
print("abc" != "abcb")  # ==>True
print("abc" in "abcb")  # ==>True
print("abc" not in "abcb")  # ==>False

# 逻辑运算符 and or not 类似C中 && || ！
print(False and True)  # ==>False
print(False or True)  # ==>True
print(not True)  # ==>False

# 一些返回值为布尔值

# 是否以xx开头/结尾
print("abc".startswith("ab"))  # ==>True
print("abc".endswith("bc"))  # ==>True

# item是否是dataType类型
print(isinstance('1', int))  # ==>False
print(isinstance(1, int))  # ==>True

str = "abc"
str.isdigit()  # 是否都是数字
str.isalpha()  # 是否都是字母
str.isalnum()  # 是否都是字母数字
str.islower()  # 至少有一个字母，所有字母是否都是小写
str.isupper()  # 至少有一个字母，所有字母是否都是大写
str.isspace()  # 仅含空白字符

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   2.if语句                               #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 单if
if True:
    print(True)
    print(True)

# if-else
if False:
    print(True)
else:
    print(False)

# 嵌套if-else
if True:
    if True:
        print(1, True)
    else:
        print(1, False)
else:
    if True:
        print(2, True)
    else:
        print(2, False)

# elif
if False:
    print(1)
elif False:
    print(2)
elif False:
    print(3)
else:
    print(4)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   3.while语句                            #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 循环10次
i = 0
while i < 10:
    i += 1
    print(i)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   4.for语句                              #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 遍历
for obj in [1, 2, 3, 4, 5]:
    continue
    print(obj)

# 制造等差数列range(first,end,步长=1)，range(len):从0开始，步长为1
for obj in range(1, 3):
    print(obj)
# ==>1
# ==>2

# 循环语句中常用语句
# continue 跳过此次循环
for obj in range(1, 5):
    if obj == 3:
        continue
    print(obj)
# ==>1
# ==>2
# ==>4

# break 跳出循环
for obj in range(1, 5):
    if obj == 3:
        break
    print(obj)
# ==>1
# ==>2

# pass 占位符语句，什么也不做
for obj in range(1, 5):
    pass