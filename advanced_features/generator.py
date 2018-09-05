# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.生成器函数                            #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 含有 yield 关键字的函数，调用该函数时会返回一个生成器。
def generator_function():
    i = 1
    while True:
        yield i
        i += 1


g = generator_function()  # 函数没有立即执行，而是返回了一个生成器，当然也是一个迭代器
print(g.__next__())  # ==>1
print(g.__next__())  # ==>2
print(g.__next__())  # ==>3
print(g.__next__())  # ==>4
#当我们使用 yield 时，它帮我们自动创建了
# __iter__() 和 __next__() 方法，
# 而且在没有数据时，也会抛出 StopIteration 异常，

# 使用 send() 方法给它发送消息
# # send() 方法就是 next() 的功能，加上传值给 yield。
def generator_function():
    i = 1
    while True:
        info = yield i
        i += 1
        print(info)

g = generator_function()
print(g.__next__())
print(g.send("发送内容"))
print(g.__next__())
print(g.__next__())
# ==>1
# ==>发送内容
# ==>2
# ==>None
# ==>3
# ==>None
# ==>4


# 使用 throw() 方法给它发送异常
def generator_function():
    i = 1
    try:
        while True:
            info = yield i
            i += 1
            print(info)
    except ValueError:
        yield 'Error'
g = generator_function()
print(g.__next__())
print(g.send("发送内容"))
print(g.throw(ValueError))
# ==>1
# ==>发送内容
# ==>2
# ==>Error


# 使用 close() 方法关闭生成器
# 再次调用 next() 方法，不管能否遇到 yield 关键字，
# 都会抛出 StopIteration 异常

def generator_function():
    i = 1
    while True:
        yield i
        i += 1

print(g.__next__())
print(g.__next__())
print(g.close())
# print(g.__next__())  # 抛出 StopIteration 异常
