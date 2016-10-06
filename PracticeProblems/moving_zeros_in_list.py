import time
import random
import copy


def timer(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        print(func.__name__, 'took', '%0.8f' % (float(time.time()) - start),
              'seconds')
        return result
    return wrapper


def main():
    eric_times = []
    lazaro_times = []
    #test = [0, 0, 0, 1, 4, 0, 0, 5, 12, 14, 0, 21]

    for i in range(50):
        test = []
        for i in range(100000):
            test.append(random.randrange(0, stop=50))
        test2 = copy.deepcopy(test)
        before_funcs = time.time()
        shift_zeroes_l(test2)
        between_funcs = time.time()
        shift_zeroes_e(test)
        after_funcs = time.time()
        lazaro_times.append(float(between_funcs - before_funcs))
        eric_times.append(float(after_funcs - between_funcs))
    laz_avg = sum(lazaro_times) / len(lazaro_times)
    eric_avg = sum(eric_times) / len(eric_times)
    print('eric:', '%0.8f' % eric_avg, 'lazaro:', '%0.8f' % laz_avg)


#@timer
def shift_zeroes_e(in_list):
    num_items_moved = 0
    length_list = len(in_list)
    for index, item in enumerate(in_list):
        if not item:
            while not in_list[index] and (num_items_moved + index) <= \
                    length_list:
                in_list.append(in_list.pop(index))
                num_items_moved += 1


#@timer
def shift_zeroes_l(num):
    length_num = len(num)
    if length_num < 2:
        return
    walker, runner = 0, 1
    while runner < length_num:
        if num[walker] != 0:
            walker += 1
            runner += 1
        elif num[runner] != 0:
            temp = num[walker]
            num[walker] = num[runner]
            num[runner] = temp
            walker += 1
            runner += 1
        else:
            runner += 1



if __name__ == '__main__':
    main()
