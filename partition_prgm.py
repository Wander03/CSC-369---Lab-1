import json
import itertools
from sys import argv


def main(file):
    with open(file, 'r', encoding='utf-8') as f:
        c = 0
        for line in f:
            c += 1
        size = c // 10
        print('size: ' + str(size))

    with open(file, 'r', encoding='utf-8') as f:
        c2 = 0
        for i in range(9):
            for line in itertools.islice(f, size * i, size * (i + 1) - 1):
                c2 += 1
            print(f'i: {i} start: {size*i} end: {size*(i+1)-1} size: {c2}')
            c2 = 0
        for line in itertools.islice(f, size * 9):
            c2 += 1
        print(c2)

            # print(size)
        # out0 = open("partition00.json", "w")
        # out1 = open("partition01.json", "w")
        # out2 = open("partition02.json", "w")
        # out3 = open("partition03.json", "w")
        # out4 = open("partition04.json", "w")
        # out5 = open("partition05.json", "w")
        # out6 = open("partition06.json", "w")
        # out7 = open("partition07.json", "w")
        # out8 = open("partition08.json", "w")
        # out9 = open("partition09.json", "w")
        #
        # c2 = 0
        # for i in range(9):
        #     for line in itertools.islice(f, c2 + 1, c2 + size):
        #         c2 += 1
        #         f.seek()





        # for i in range(9):
        #     with open(f'partition0{i}.json', 'w') as out:
        #         for line in partitions[i]:
        #             json.dump(line, out)


if __name__ == '__main__':
    # main(argv[1])
    main('2021-04-03-15.json')
    # main('partition00.json')
