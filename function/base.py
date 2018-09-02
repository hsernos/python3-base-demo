# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.定义函数                              #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

def hello1():
    """ 无参函数"""
    return "hello"


def hello2(name):
    """有参函数"""
    return name


def hello3():
    """无返回值返回None"""
    pass


def hello4(x, y, z):
    """多个返回值的函数"""
    return x, y, z


print(hello1())  # ==>hello
print(hello2("Tom"))  # ==>Tom
print(hello3())  # ==>None
print(hello4(1, 2, 3), type(hello4(1, 2, 3)))  # ==>(1, 2, 3) <class 'tuple'>


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   2.函数参数                              #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

def add1(x, y):
    """x,y为必选参数"""
    print(x + y)


def add2(x, y, z=1):
    """
    默认参数必须放在必选参数后面
    """
    print(x + y + z)


def add3(L=[]):
    """
    默认参数为可变对象时会出问题
    连续不给默认参数传值两次就会出现问题
    建议使用不可变对象
    """
    L.append('End')
    print(L)


def add4(*nums):
    """可变参数类型就是元组"""
    sum = 0
    for x in nums:
        sum += x
    print("sum =", sum, ",可变参数类型:", type(nums))


def add5(**kwargs):
    """关键字参数类型就是字典"""
    sum = 0
    for k, v in kwargs.items():
        sum += v
    print(sum, kwargs)


def show(x, y, z=3, *args, **kwargs):
    """
    参数组合在使用的时候是有顺序的，
    依次是必选参数、默认参数、可变参数和关键字参数。
    """
    print('x =', x)
    print('y =', y)
    print('z =', z)
    print('args =', args)
    print('kwargs =', kwargs)


add1(1, 2)  # ==>3
add2(1, 2)  # ==>4
add2(1, 2, 3)  # ==>6
add3()  # ==>['End']
add3()  # ==>['End', 'End']
add4(1, 2)  # ==>sum = 3 ,可变参数类型: <class 'tuple'>
add5(x=1, y=2)  # ==>3 {'x': 1, 'y': 2}
show(1, 2)
# ==>x = 1
# ==>y = 2
# ==>z = 3
# ==>args = ()
# ==>kwargs = {}
show(1, 2, 4, 5, 6, v=2, f=3)
# ==>x = 1
# ==>y = 2
# ==>z = 4
# ==>args = (5, 6)
# ==>kwargs = {'v': 2, 'f': 3}
