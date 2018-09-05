# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.super                                 #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 单向继承
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am %s.' % self.name)

class Dog(Animal):
    def greet(self):
        super().greet()   # Python2 可使用 super(Dog, self).greet()
        print('WangWang...')

dog = Dog('dog')
dog.greet()
# ==>Hello, I am dog.
# ==>WangWang...


# 菱形继承
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")

c = C()
# ==>enter C
# ==>enter A
# ==>enter B
# ==>enter Base
# ==>leave Base
# ==>leave B
# ==>leave A
# ==>leave C

"""
super 和父类没有实质性的关联
事实上，对于你定义的每一个类，
Python 会计算出一个方法解析顺序
（Method Resolution Order, MRO）列表，
它代表了类继承的顺序，我们可以使用下面的方式获得某个类的 MRO 列表：
"""
print(C.mro())  # ==>[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   2.元类（metaclass）                     #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
"""
元类（metaclass）是用来创建类（对象）的可调用对象。
元类的主要目的是为了控制类的创建行为。
type 就是一个元类
"""

class Base(object):
    pass

# 类的创建
class Foo(Base):
   foo = True

# 改用 type 来创建
Foo1 = type("Foo1",(Base,),{"foo":True})
print(Foo)  # ==><class '__main__.Foo'>
print(Foo1)  # ==><class '__main__.Foo1'>

# 定义元类，给类的所有方法和属性前面加上my_
class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 给所有属性和方法前面加上前缀 my_
        _attrs = (('my_' + name, value) for name, value in attrs.items())
        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加了一个 echo 方法

        return type.__new__(cls, name, bases, _attrs)  # 返回创建后的类

# 普通类使用元类
class Foo(metaclass=PrefixMetaclass):
    # __metaclass__ = PrefixMetaclass  # Python2中加入此属性，删除参数metaclass=PrefixMetaclass
    name = 'foo'
    def bar(self):
        print('bar')

f = Foo()
print(f.my_name)  # ==>foo


# 继承类使用元类
class Foo(object,metaclass=PrefixMetaclass):
    name = 'foo'
    def bar(self):
        print('bar')

class Bar(Foo):
    prop = 'bar'

# 定义 class Bar(Foo) 时,Python沿着__metaclass__MRO 列表查找__metaclass__，
# 如果还是找不到，就会用 type 来创建这个类。
b = Bar()
print(b.my_prop)  # ==>bar
