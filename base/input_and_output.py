# 1.输出函数print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("-------------------------------------")
print("str")  # ==>str
# 以空格连接
print("str1", "str2", "str3")  # ==>str1 str2 str3
# 以sep参数连接，默认一个空格
print("str1", "str2", "str3", sep=',')  # ==>str1,str2,str3
# 以end参数结尾,默认换行
print("str1", "str2", "str3", end='$\n')  # ==>str1 str2 str3$

print("-------------------------------------")
# 格式化输出,//+:正负//0:用 0 填充空白//n.m:字段宽度 n，精度 m//
num = 1.22
str = "中国"
print("num1=%0+10.3f,num2=%s" % (num, str))  # ==>num1=+00001.220,num2=中国

# 2.输入函数input('')

print("-------------------------------------")
# 输入是字符串类型，数字须强转
a = input("请输入:")  # ==>请输入:<==21
print(type(a))  # ==><class 'str'>
print(type(int(a)))  # ==><class 'int'>
