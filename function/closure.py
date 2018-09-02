# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   1.闭包                                 #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 在 Python 中，函数也是一个对象。因此，我们在定义函数时，
# 可以再嵌套定义一个函数，并将该嵌套函数返回，返回的内部函数称为闭包
def power(n):
    def compute(x):
        return x ** n
    return compute


fun1 = power(2)
fun2 = power(3)
fun3 = power(2)
# 删除原函数，闭包引用的自由变量任然存在
del power
print(fun1(3))  # ==>9
print(fun2(3))  # ==>27
# 传入的相同参数，闭包实例不同
print(fun2 == fun3)  # ==>False


# 一些误区
def count():
    funcs = []
    for i in [1, 2, 3]:
        def f():
            return i
        funcs.append(f)
    return funcs


f1, f2, f3 = count()
# 你可能认为返回结果是 1, 2, 3.事实上却不是
# 上面的函数 f 引用了变量 i，但函数 f 并非立刻执行，
# 当 for 循环结束时，此时变量 i 的值是3，
# funcs 里面的函数引用的变量都是 3.

print(f1(), f2(), f3())  # ==>3 3 3

# 解决思路：使用lambda表达式返回函数
def count():
    funcs = []
    for i in [1, 2, 3]:
        def g(param):
            return lambda : param
        funcs.append(g(i))
    return funcs


f1, f2, f3 = count()
print(f1(), f2(), f3())  # ==>1 2 3

