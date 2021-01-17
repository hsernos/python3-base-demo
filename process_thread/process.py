from time import sleep, ctime
from multiprocessing import Process, Pool, Queue
import os, random
from concurrent.futures import ProcessPoolExecutor

def loop(num, nsec):
    print('Parent process %s.' % os.getpid())
    print('start loop{} at: '.format(num), ctime())
    sleep(nsec)
    print('loop{} done at: '.format(num), ctime())


l = [2, 4, 3, 2, 4]
l_len = len(l)


# 多进程
def multi_process():
    ps = []
    for i in range(0, l_len):
        p = Process(target=loop, args=(i, l[i]))
        ps.append(p)
    for i in range(0, l_len):
        ps[i].start()
    for i in range(0, l_len):
        ps[i].join()


# 进程池
def process_pool():
    # Pool的默认大小是CPU的核数
    p = Pool(4)
    for i in range(l_len):
        p.apply_async(loop, args=(i, l[i]))
    # 调用close()之后就不能继续添加新的Process了
    p.close()
    # 调用join()之前必须先调用close()
    p.join()


# 进程池另一种实现
def process_pool1():
    with ProcessPoolExecutor(3) as executor:
        for i in range(l_len):
            executor.submit(loop, i, l[i])


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


#  进程间通信
def process_queue():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    process_queue()
