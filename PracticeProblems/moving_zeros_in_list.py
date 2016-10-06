import time
def main():
    in_list = [0, 0, 0, 1, 2, 0, 3, 13, 15, 12, 0, 45, 22, 0, 51, 100, 0, 4,
               136, 0, 0, 0, 54]

    print(in_list)
    start = float(time.time())
    move_zeros(in_list)
    end = float (time.time())

    print(in_list)
    print('process took:', '%0.8f' % (end-start))


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
