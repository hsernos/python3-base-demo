# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.定义类                                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 定义类及成员变量
class Animal():
    # 有静态方法或类方法时将变量放在外面，一般在__init__方法中定义成员变量
    sex = "man"  # 定义公有属性,还可通过Animal.sex设置或得到值,不建议
    __password = "123456"  # 定义私有属性,不建议

    # 初始化方法，类似c++的构造函数
    def __init__(self, name, age):
        # __xxx__是特殊变量，不推荐使用,效果同公有变量
        # xxx是公有变量，推荐使用
        # __xxx是私有变量，推荐使用
        self.name = name  # 定义公有属性，建议
        self.__age = age  # 定义私有属性,两个下划线代表私有，建议


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
#                   3.定制类和魔法方法                      #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
