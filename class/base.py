# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.定义类                                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 定义类及成员变量
class Animal():
    # 有静态方法或类方法时将变量放在外面，一般在__init__方法中定义成员变量
    sex = "man"  # 定义公有类变量,可通过Animal.sex设置或得到值
    __password = "123456"  # 定义私有类变量

    # 初始化方法，类似c++的构造函数
    def __init__(self, name, age):
        # __xxx__是特殊变量，不推荐使用,效果同公有变量
        # xxx是公有变量，推荐使用
        # __xxx是私有变量，推荐使用
        self.name = name  # 定义公有成员变量
        self.__age = age  # 定义私有成员变量,两个下划线代表私有


# 获取实例，访问属性
animal = Animal("dog1",6)
print(animal.__dict__)  # ==>{'name': 'dog1', '_Animal__age': 6}
print(animal.sex)  # ==>man
print(Animal.sex)  # ==>man

# 获取对象的相应类型
print(type(animal))  # ==><class '__main__.Animal'>

# isinstance(obj, type) 判断对象是否为指定的 type 类型的实例
print(isinstance(animal,Animal))  # ==>True

# hasattr/getattr/setattr方法
# # hasattr(obj, attr)
print(hasattr(animal, "sex"))  # ==>True
print(hasattr(animal, "age"))  # ==>False<== 私有变量返回为False

# # getattr(obj, attr[, default])
print(getattr(animal, "sex"))  # ==>man<==没有该属性，也没有默认值，抛AttributeError
print(getattr(animal, "attr", "默认值"))  # ==>默认值<== 没有该属性则返回默认值

# # setattr(obj, attr, value)
setattr(animal, "sex", "woman")
print(animal.sex)  # ==>woman

# dir(obj),获取相应对象的所有属性和方法名的列表
print(dir(animal)) # ==>['_Animal__age', '_Animal__password', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'sex']


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   2.继承和多态                            #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Animal继承object
class Animal(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, I am %s." % self.name)

# Dog继承Animal
class Dog(Animal):
    def greet(self):  # 重载
        return 'WangWang.., I am %s. ' % self.name

# Cat继承Animal
class Cat(Animal):  # 重载
    def greet(self):
        return 'MiaoMiao.., I am %s. ' % self.name

dog1 = Dog("xiaogou")
print(dog1.get_name())  # ==>xiaogou<== 调用父类方法
print(dog1.name)  # ==>xiaogou<== 调用父类函数
print(dog1.greet())  # ==>WangWang.., I am xiaogou.<== 调用子类重载方法

# 多态函数
def hello(animal):
    print(animal.greet())

# 多态: 根据对象调用相同的函数作出不同的反应
hello(Dog("xiaogou"))  # ==>WangWang.., I am xiaogou.
hello(Cat("xiaomao"))  # ==>MiaoMiao.., I am xiaomao.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   3.类方法和静态方法                      #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

class A:
    name = "A.."
    @classmethod  # 类方法装饰器
    def foo(cls):
        print('hello',cls.name)

A.foo()  # ==>hello A..<==类方法


class B:
    name = "B.."
    @staticmethod  # 静态方法装饰器
    def static_foo():
        print('hello',B.name)

B.static_foo()  # ==>hello B..<==静态方法


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   4.定制类和魔法方法                       #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 常用魔法方法（特殊方法）

# # __new__，创建实例时会先调用__new__(cls[, ...])创建实例，再用__init__方法对该实例进行初始
# # 重载__new__类方法需要返回类的实例
class A(object):
    obj = None  # 类变量
    def __new__(cls):
        if A.obj != None:
            return A.obj  # 重复创建返回obj中存储的初始对象
        else:
            return object.__new__(cls)  # 第一次创建初始对象

    def __init__(self):
        A.obj = self  # 第一次将初始对象存入obj变量

print(A())  # ==><__main__.A object at 0x000001C33D91DC50>
print(A())  # ==><__main__.A object at 0x000001C33D91DC50><==对象相同，即单例

# #  __str__ , __repr__
class Foo(object):
    def __init__(self, name):
        self.name = name

print (Foo('ethan'))  # ==><__main__.Foo object at 0x0000018CE856DDD8>

class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 类似java中的toString
        return "__str__"

    def __repr__(self):
        return "__repr__"

f = Foo('ethan')
print(f)  # ==>__str__
# >>> f
# __repr__






class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 返回迭代器对象本身
        return self

    def __next__(self):  # 返回容器下一个元素
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __getitem__(self, n):  # 返回第n个元素
        if isinstance(n, slice):  # 如果 n 是 slice 对象，切片
            a, b = 1, 1
            start, stop = n.start, n.stop
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        if isinstance(n, int):  # 如果 n 是 int 型
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a

# # __iter__
"""
对象用于for...in循环，须定义__iter__和__next__(Python2是next方法)
__iter__ 返回迭代对象， __next__ 返回下一个元素
"""

fib = Fib()
list = []
for i in fib:
    if i > 10:
        break
    print(i)
    list.append(i)
print(list)  # ==>[1, 1, 2, 3, 5, 8]

# #  __getitem__ , __setitem__ , __delitem__
"""
__getitem__ 用于用中括号获取值
__setitem__ 用于用中括号设置值
__delitem__ 用于用中括号删除值

"""
print(fib[0],fib[1],fib[3],fib[4])  # ==>1 1 3 5
print(fib[0:6])  # ==>[1, 1, 2, 3, 5, 8]

class Point(object):
    def __init__(self):
        self.coordinate = {}

    def __str__(self):
        return "point(%s)" % self.coordinate

    def __getitem__(self, key):
        return self.coordinate.get(key)

    def __setitem__(self, key, value):
        self.coordinate[key] = value

    def __delitem__(self, key):
        del self.coordinate[key]
        print ('delete %s' % key)

    def __len__(self):
        return len(self.coordinate)

    def __call__(self, n):
        return n

    __repr__ = __str__

p = Point()
p['x'] = 2    # 对应于 p.__setitem__('x', 2)
p['y'] = 5    # 对应于 p.__setitem__('y', 5)
len(p)        # 对应于 p.__len__
p['x']        # 对应于 p.__getitem__('x')
del p['x']    # 对应于 p.__delitem__('x')

# __getattr__ , __setattr__ , __delattr__
"""
当访问/设置/删除不存在的属性时，会分别调用这三个函数
"""


# __call__
"""
对实例进行类似函数的调用
"""

p = Point()
print(p(4))  # ==>4<==传入参数，对实例进行调用，对应 p.__call__(4)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   5.基于类的装饰器                        #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

class Bold(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return '<b>' + self.func(*args, **kwargs) + '</b>'

@Bold
def hello(name):
    return 'hello %s' % name

print(hello("world"))  # ==><b>hello world</b>


# 如果类装饰器有参数，则 __init__ 接收参数，而 __call__ 接收 func

class Tag(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            return "<{tag}>{res}</{tag}>".format(
                res=func(*args, **kwargs), tag=self.tag
            )
        return wrapped

@Tag('b')
def hello(name):
    return 'hello %s' % name

print(hello("world"))  # ==><b>hello world</b>


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   6.slots 魔法                            #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point(3, 4)
p.z = 5    # 绑定了一个新的属性
print(p.z)  # ==>5

"""
创建了实例 p 之后，给它绑定了一个新的属性 z，
这种动态绑定的功能虽然很有用，但它的代价是消耗了更多的内存。
可以使用 __slots__ 来告诉 Python 只给一个固定集合的属性分配空间
__slots__ 设置的属性仅对当前类有效，对继承的子类不起效
"""

class Point(object):
    __slots__ = ('x', 'y')       # 只允许使用 x 和 y,使用其他属性会报错

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point(3, 4)
# p.z = 5

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   7.属性的get，set装饰器                  #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

class Exam(object):
    def __init__(self, score):
        self._score = score

    @property  # get属性
    def score(self):
        return self._score

    @score.setter  # set属性
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

e = Exam(60)
print(e.score)  # ==>60
e.score = 110
print(e.score)  # ==>100
