from time import sleep, ctime
import threading
from concurrent.futures import ThreadPoolExecutor


def loop(num, nsec):
    print('start loop{} at: '.format(num), ctime())
    sleep(nsec)
    print('loop{} done at: '.format(num), ctime())


l = [2, 4, 3, 2, 4]
l_len = len(l)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   1.多线程                                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 多线程, 应用IO密集型任务，因为GIL保证同时只能有一个线程运行
def multi_thread():
    ps = []
    for i in range(0, l_len):
        p = threading.Thread(target=loop, args=(i, l[i]))
        ps.append(p)
    for i in range(0, l_len):
        ps[i].start()
    for i in range(0, l_len):
        ps[i].join()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   2.线程池                                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


def thread_pool():
    with ThreadPoolExecutor(3) as executor:
        for i in range(l_len):
            executor.submit(loop, i, l[i])


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   3.锁                                   #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


lock1 = threading.Lock()


def loop1(num, nsec):
    lock1.acquire()  #获得锁
    print('start loop{} at: '.format(num), ctime())
    sleep(nsec)
    print('loop{} done at: '.format(num), ctime())
    lock1.release()  #释放锁


def lock():
    ps = []
    for i in range(20):
        t = threading.Thread(target=loop1, args=(i, 2))  # 实例化一个线程
        ps.append(t)
    for i in range(20):
        ps[i].start()
    for i in range(20):
        ps[i].join()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   4.信号量                                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

s1 = threading.Semaphore(5)


def loop2(num, nsec):
    s1.acquire()  #计数器获得锁
    print('start loop{} at: '.format(num), ctime())
    sleep(nsec)
    print('loop{} done at: '.format(num), ctime())
    s1.release()  #计数器释放锁


def semaphore():
    ps = []
    for i in range(20):
        t = threading.Thread(target=loop2, args=(i, 2))  # 实例化一个线程
        ps.append(t)
    for i in range(20):
        ps[i].start()
    for i in range(20):
        ps[i].join()


if __name__ == '__main__':
    print("------------")
    lock()
    print("------------")