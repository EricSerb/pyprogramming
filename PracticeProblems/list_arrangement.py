def main():
    in_list = [3, 4, 2, 1, 7, 6, 8]
    out_list = rearrange(in_list)

    print(in_list)
    print(out_list)


def rearrange(in_list):
    out_list = [x for x in in_list if x % 2 == 0]
    for x in in_list:
        if x % 2 == 1:
            out_list.append(x)
    return out_list

if __name__ == '__main__':
    main()
