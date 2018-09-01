# ++++++++++++++++++
# 1.输出函数print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# ++++++++++++++++++

print("str")  # ==>str

# 以空格连接
print("str1", "str2", "str3")  # ==>str1 str2 str3

# 以sep参数连接，默认一个空格
print("str1", "str2", "str3", sep=',')  # ==>str1,str2,str3

# 以end参数结尾,默认换行
print("str1", "str2", "str3", end='$\n')  # ==>str1 str2 str3$


# 类似C语言的格式化输出,//+:正负//0:用 0 填充空白//n.m:字段宽度 n，精度 m//
num = 1.22
str = "中国"
print("num1=%0+10.3f,num2=%s" % (num, str))  # ==>num1=+00001.220,num2=中国

# 使用format进行格式化输出
# {对应参数号:[<,^,>,(左,居中,右)]宽度[n,s,d,f,%(数字,字符串,整数，浮点数，百分数)]}
print("{0:<5n}{0:<5n}{1:^5s}{2:>5s}".format(1,"dd","dd"))  # ==>1    1     dd     dd

# 默认右对齐,[,]表示千位符,[.num]表示四舍五入保留num小数
print("{0:10,d}".format(123456))  # ==>   123,456
print("{0:10,.3f}".format(123.45678))  # ==>   123.457
print("{0:10.3%}".format(3.456))  # ==>  345.600%


# ++++++++++++++++++
# 2.输入函数input('')
# ++++++++++++++++++

# 输入是字符串类型，数字须强转
a = input("请输入:")  # ==>请输入:<==21
print(type(a))  # ==><class 'str'>
print(type(int(a)))  # ==><class 'int'>
