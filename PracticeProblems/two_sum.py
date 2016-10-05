def main():
    in_list = [-1, 6, 3, 5, -2, 0, -1, 4]
    target = 3

    pairs = move_zeros(in_list, target)

    print(pairs)


def move_zeros(in_list, target):
    out_list = []
    for index, item in enumerate(in_list):
        for i in in_list[index+1:]:
            if (item + i) == target:
                if [item, i] not in out_list and [i, item] not in out_list:
                    out_list.append([item, i])
    return out_list

if __name__ == '__main__':
    main()