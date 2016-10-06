def main():
    in_list = [(0, 0), (5, 10), (3, 7), (5, 12), (-2, -4), (0, 2), (-1, 6)]

    print('list:', in_list)
    print('centroid:', centroid(in_list))


def centroid(in_list):
    x_coor = [x[0] for x in in_list]
    y_coor = [y[1] for y in in_list]
    # remove int call to make them doubles
    return tuple((int(sum(x_coor) / len(in_list)), int(sum(y_coor) / len(
        in_list))))

if __name__ == '__main__':
    main()
