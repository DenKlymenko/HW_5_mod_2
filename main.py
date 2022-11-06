from multiprocessing import Process
from time import time


def factorize(*numbers):
    timer = time()
    general_array = [[] for i in range(len(numbers))]
    index = 0
    for number in numbers:
        for i in range(1, number+1):
            if number % i == 0:
                general_array[index].append(i)
        print(number, general_array[index])
        index += 1
    print('Done', time() - timer)
    return general_array


a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
             1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


p1 = Process(target=factorize, args=(128, ))
p2 = Process(target=factorize, args=(255, ))
p3 = Process(target=factorize, args=(99999, ))
p4 = Process(target=factorize, args=(10651060, ))

p1.start()
p2.start()
p3.start()
p4.start()

