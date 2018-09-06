# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.文本读取                              #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# open 函数的常用模式：
"""
'r' ：只读，无文件报错
'r+'：读写（覆盖），无文件报错
'w' ：只写（覆盖），无文件创建
'w+'：读写（覆盖），无文件创建
'a' ：只写（追加），无文件创建
'a+'：读写（追加），无文件创建

'b' :二进制模式（可添加到其他模式中使用）
"""

# 读取所有内容
with open("data/read.txt","r") as f:  # 使用with，最后自动运行f.close()关闭文件
    read_data = f.read
    f.seek(0)  # 将文件指针指向文件开头
    readlines_data = f.readlines()

print(read_data)
# ==>1   2   3
# ==>4   5   6
# ==>7   8   9

print(readlines_data)
# ==>['1   2   3\n', '4   5   6\n', '7   8   9']

print(list(open("data/read.txt","r")))
# ==>['1   2   3\n', '4   5   6\n', '7   8   9']

# 按字节读取
with open('data/read.txt', 'r') as f:
    while True:
        piece = f.read(1024)        # 每次读取 1024 个字节（即 1 KB）的内容
        if not piece:
            break
        print(piece)
# ==>1   2   3
# ==>4   5   6
# ==>7   8   9


# 逐行读取
with open('data/read.txt', 'r') as f:
    while True:
        line = f.readline()     # 逐行读取
        if not line:
            break
        print(line,end='')  # end='':避免 print 自动换行
    print()
# ==>1   2   3
# ==>4   5   6
# ==>7   8   9

with open('data/read.txt', 'r') as f:
    for line in f:  # 文件对象是可迭代的,并且是逐行迭代
        print(line, end='')
    print()
# ==>1   2   3
# ==>4   5   6
# ==>7   8   9

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   2.文本写入                              #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 覆盖写文件
with open('data/write.txt', 'w+') as f:
    f.write('one\n')
    f.write('two')
    f.seek(0)
    data = list(f)

print(data)
# ==>['one\n', 'two']

# 追加写文件
with open('data/write.txt', 'a+') as f:
    f.write('\nthree\n')
    f.write('four')
    f.seek(0)
    data = list(f)

print(data)
# ==>['one\n', 'two\n', 'three\n', 'four']
