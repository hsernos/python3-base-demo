from functools import wraps


## 简单的协程
def simple_coroutine():
    while True:
        print('start')
        x = yield
        print('received:', x)


s = simple_coroutine()
# 激活协程,效果等同于s.send(None)
next(s)
s.send(42)
# ==>start
# ==>received: 42
# ==>start


## 计算平均值
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))  # ==>10.0
print(coro_avg.send(30))  # ==>20.0
print(coro_avg.send(5))  # ==>15.0


## 带预激的装饰器
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager1():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager1()
print(coro_avg.send(10))  # ==>10.0
print(coro_avg.send(30))  # ==>20.0
print(coro_avg.send(5))  # ==>15.0
coro_avg.close()

from collections import namedtuple

Result = namedtuple('Result', 'count average')


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
    average = total / count
    return Result(count, average)


# 委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    print(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}
if __name__ == '__main__':
    main(data)
