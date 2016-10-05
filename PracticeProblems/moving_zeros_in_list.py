def main():
    in_list = [0, 0, 0, 1, 2, 0, 3, 13, 15, 12]

    print(in_list)

    move_zeros(in_list)

    print(in_list)


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
