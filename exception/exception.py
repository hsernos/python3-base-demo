# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.异常处理                              #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 使用 try/except 捕捉异常
"""
try...except...
try...except...else...
try...except...else...finally...
try...except...except...else...finally...
try...finally...
"""


class SomeError(BaseException):
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        pass


try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:  # 捕获 TypeError 异常
    print('TypeError:', e)
except BaseException as e:  # 捕获其他异常
    print('BaseException:', e)
    raise SomeError("自定义异常") # 抛出自定义异常
else:  # 无异常时执行
    print("no error")
finally:  # 无论有无异常，都执行
    print("无论有无异常，都执行")
# ==>division by zero
# ==>无论有无异常，都执行


