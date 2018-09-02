from functools import wraps

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   1.装饰器                               #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 给hello world两边加上<i></i>标签
# 闭包实现装饰器，makeitalic是一个装饰器
def hello():
    return 'hello world'
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

hello = makeitalic(hello)
print(hello())  # ==><i>hello world</i>
print(hello.__name__)  # ==>wrapped


# 使用@语法糖（Syntactic Sugar）简化
@makeitalic
def hello1():
    return 'hello world'

print(hello1())  # ==><i>hello world</i>
print(hello1.__name__)  # ==>wrapped


# 多层嵌套
def makeitalic_one(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

def makeitalic_two(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

@makeitalic_one
@makeitalic_two
def func():
    return "python"

# 等同于 func = makeitalic_one(makeitalic_two(func))
print(func())  # ==><i><b>python</b></i>


# 语法糖上加参数
def wrap_in_tag(tag):
    def makeitalic(func):
        def wrapped():
            return "<" + tag + ">" + func() + "</" + tag + ">"
        return wrapped
    return makeitalic

@wrap_in_tag("div")
def fun1():
    return "python"

print(fun1())  # ==><div>python</div>


#  含有参数的被装饰函数

def decorator(func):
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '<i>' + ret + '</i>'
    return wrapped

@decorator
def fun2(name):
    return "hello " + name

@decorator
def fun3(name, other):
    return "hello " + name + "," + other
print(fun2("world"))  # ==><i>hello world</i>
print(fun3("world","I'm coming"))  # ==><i>hello world,I'm coming</i>

# 装饰器的副作用
# 它的函数名称已经不是原来的名称
print(fun3.__name__)  # ==>wrapped

# 为了消除这样的副作用，Python 中的 functool 包提供了一个 wraps 的装饰器：
# from functools import wraps

def makeitalic(func):
    @wraps(func)
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeitalic
def hello():
    return "hello world"

print(hello.__name__)  # ==>hello

# 此外，还可用类去装饰函数，demo见类的那一节