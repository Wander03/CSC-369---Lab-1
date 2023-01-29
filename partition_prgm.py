import json
from sys import argv


def read_lines(file):
    for line in file:
        # yield returns each iteration, then resumes going through the for loop (good for not reading large files
        # into memory)
        yield json.loads(line)


def main(file):
    with open(file, 'r', encoding='utf-8') as f:
        line_count = sum(1 for line in f)
        # Return cursor to beginning of file
        f.seek(0)

        partition_size = line_count // 10
        ranges = {}

        for partition in range(10):
            start = -1
            end = -1
            with open(f'partition0{partition}.json', 'w') as out:
                for i, line in enumerate(read_lines(f)):
                    if i == 0:
                        start = line['id']
                    end = line['id']
                    if (i < partition_size) or (i == 9):
                        json.dump(line, out)
                        out.write('\n')
                    else:
                        ranges[f'partition0{partition}'] = {'first_id': start, 'last_id': end}
                        break
            ranges['partition09'] = {'first_id': start, 'last_id': end}

    with open('index.json', 'w') as f:
        json.dump(ranges, f)


if __name__ == '__main__':
    main(argv[1])
    # main('2021-04-03-15.json')
