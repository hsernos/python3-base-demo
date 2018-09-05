from math import sqrt, pow
from contextlib import contextmanager
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.上下文管理器                          #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 上下文管理器协议: 要实现对象的 __enter__() 和 __exit__() 方法。

class Point(object):
    def __init__(self, x, y):
        print('initialize x and y')
        self.x, self.y = x, y

    def __enter__(self):
        """
        返回值赋给 as 字句中的变量
        """
        print("Entering context")
        return self

    def __exit__(self, type, value, traceback):
        """
        如果退出时没有发生异常，则type, value 和 traceback 都为None
        如果发生异常，返回 True 表示不处理异常，
        否则会在退出该方法后重新抛出异常以由 with 语句之外的代码逻辑进行处理
        """
        print("Exiting context")

    def get_distance(self):
        distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return distance

with Point(3,4) as pt:
    print('distance: ', pt.get_distance())
# ==>initialize x and y   # 调用了 __init__ 方法
# ==>Entering context     # 调用了 __enter__ 方法
# ==>distance:  5.0       # 调用了 get_distance 方法
# ==>Exiting context      # 调用了 __exit__ 方法


# 内建对象使用 with 语句

# # 传统的文件操作经常使用 try/finally
file = open('somefile', 'r')
try:
    for line in file:
        print(line)
finally:
    file.close()     # 确保关闭文件

# # 将上面的代码改用 with 语句：
with open('somefile', 'r') as file:
    for line in file:
        print(line)


# contextlib 模块

@contextmanager
def point(x, y):
    print('before yield')
    yield x * x + y * y
    print('after yield')

with point(3, 4) as value:
    print('value is: %s' % value)

# ==>before yield
# ==>value is: 25
# ==>after yield