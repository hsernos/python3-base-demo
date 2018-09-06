import os

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.常见的文件和目录操作                  #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

"""
os.mkdir                创建目录
os.rmdir                删除目录
os.rename               重命名
os.remove               删除文件
os.getcwd               获取当前工作路径
os.walk	                 遍历目录
os.path.join            连接目录与文件名
os.path.split           分割文件名与目录
os.path.abspath         获取绝对路径
os.path.dirname         获取路径
os.path.basename        获取文件名或文件夹名
os.path.splitext        分离文件名与扩展名
os.path.isfile	          判断给出的路径是否是一个文件
os.path.isdir           判断给出的路径是否是一个目录
"""
# 以下绝对路径仅供参考

# 获取文件或目录的绝对路径
print(os.path.abspath('bin.py'))
print(os.path.abspath('data'))
print(os.path.abspath('.'))
# ==>E:\py\python3-demo\io\bin.py
# ==>E:\py\python3-demo\io\data
# ==>E:\py\python3-demo\io

# 获取文件或文件夹的路径
print(os.path.dirname('E:\\py\\python3-demo\\io\\bin.py'))
print(os.path.dirname('E:\\py\\python3-demo\\io\\'))
print(os.path.dirname('E:\\py\\python3-demo\\io'))
# ==>E:\py\python3-demo\io
# ==>E:\py\python3-demo\io
# ==>E:\py\python3-demo

# 获取文件名或文件夹名
print(os.path.basename('E:\\py\\python3-demo\\io\\bin.py'))
print(os.path.basename('E:\\py\\python3-demo\\io\\'))
print(os.path.basename('E:\\py\\python3-demo\\io'))
# ==>bin.py
# ==>
# ==>io

# 分离文件名与扩展名
print(os.path.splitext('E:\\py\\python3-demo\\io\\bin.py'))
print(os.path.splitext('E:\\py\\python3-demo\\io\\'))
print(os.path.splitext('E:\\py\\python3-demo\\io'))
# ==>('E:\\py\\python3-demo\\io\\bin', '.py')
# ==>('E:\\py\\python3-demo\\io\\', '')
# ==>('E:\\py\\python3-demo\\io', '')

# 分离目录与文件名
print(os.path.split('E:\\py\\python3-demo\\io\\bin.py'))
print(os.path.split('E:\\py\\python3-demo\\io\\'))
print(os.path.split('E:\\py\\python3-demo\\io'))
# ==>('E:\\py\\python3-demo\\io', 'bin.py')
# ==>('E:\\py\\python3-demo\\io', '')
# ==>('E:\\py\\python3-demo', 'io')

# 判断是否文件/目录
print(os.path.isfile('E:\\py\\python3-demo\\io\\bin.py'))
print(os.path.isdir('E:\\py\\python3-demo\\io\\'))
print(os.path.isdir('E:\\py\\python3-demo\\io'))
# ==>True
# ==>True
# ==>True


# 遍历目录，os.walk返回(dirpath, dirnames, filenames)
for root, dirs, files in os.walk('E:\\py\\python3-demo\\io'):
    print(root)
    print(dirs)
    print(files)
# ==>E:\py\python3-demo\io
# ==>['data']
# ==>['bin.py', 'os.py', 'text.py']
# ==>E:\py\python3-demo\io\data
# ==>[]
# ==>['read.txt', 'test.jpg', 'test2.png', 'write.txt']
