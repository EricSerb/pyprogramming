import itertools


def main():
    in_list = [-1, 6, 3, 5, -2, 0, -1, 4]
    target = 3

    pairs = two_sum(in_list, target)
    sets = targetSum(in_list, target)

    print(pairs)
    print(sets)


def two_sum(in_list, target):
    out_list = []
    for index, item in enumerate(in_list):
        for i in in_list[index+1:]:
            if (item + i) == target:
                if [item, i] not in out_list and [i, item] not in out_list:
                    out_list.append([item, i])
    return out_list


def targetSum(L, r):
    """
    @Programmer = Arturo Valery
    """
    return set((a,b) if a<=b else (b,a) for a,b in itertools.combinations(L, 2) if a+b == r)

if __name__ == '__main__':
    main()