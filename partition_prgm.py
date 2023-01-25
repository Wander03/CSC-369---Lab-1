import json
from sys import argv


def main(file):
    data = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
        print(json.dumps(data[1], indent=4))


if __name__ == '__main__':
    main(argv[1])
