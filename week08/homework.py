import time
import math
from functools import reduce

# 作业一
# 容器序列：list, tuple, dict, collections.deque
# 扁平序列：str
# 可变序列：list, dict, collections.deque
# 不可变序列：tuple, str


#作业二
def mymap(func, items):
    for item in items:
        yield func(item)


#作业三
def timer(func):

    def inner(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()
        print(f'{func.__name__} runtiem: {end - start} !!!')
        return result

    return inner


@timer
def mysum(num):
    return reduce(lambda x, y: x + y, num)


if __name__ == '__main__':
    print(mysum(mymap(lambda x: math.sqrt(x), range(99999))))