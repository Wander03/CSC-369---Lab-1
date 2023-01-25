import json
from sys import argv
import matplotlib.pyplot as plt
import numpy as np


def main(file):
    data = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
        # print(json.dumps(data[0], indent=4))
        # print(json.dumps(data[-1], indent=4))
    print(len(data))
    # partitions = np.array_split(np.asarray(data), 10)
    # for i in range(0, 10):
    #     with open(f'partition0{i}.json', 'w', encoding='utf-8') as f:
    #         for line in partitions[i]:
    #             f.write(f'{line}\n')

    # ids = []
    # for i in data:
    #     ids.append(int(i['id']))

    # Make a Histogram of the Ids --> was a uniform dist.
    # plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    #
    # x = np.asarray(ids)
    # plt.hist(x, bins=10)
    # plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
    # plt.show()


if __name__ == '__main__':
    # main(argv[1])
    # main('2021-04-03-15.json')
    main('partition00.json')
