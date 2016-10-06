import time
import random


def timer(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        print(func.__name__, 'took', '%0.8f' % (float(time.time()) - start),
              'seconds')
        return result
    return wrapper


def main():
    in_list = [0, 0, 0, 1, 2, 0, 3, 13, 15, 12, 0, 45, 22, 0, 51, 100, 0, 4,
               136, 0, 0, 0, 54]
    test = []
    for i in range(100000):
        test.append(random.randrange(0, stop=50))

    # print(test)
    # start = float(time.time())
    move_zeros(test)
    move_zeros(in_list)
    # end = float(time.time())

    # print(test)
    # print('process took:', '%0.8f' % (end-start))


@timer
def move_zeros(in_list):
    num_items_moved = 0
    for index, item in enumerate(in_list):
        if not item:
            while not in_list[index] and (num_items_moved + index) <= len(
                    in_list):
                in_list.append(in_list.pop(index))
                num_items_moved += 1

if __name__ == '__main__':
    main()
