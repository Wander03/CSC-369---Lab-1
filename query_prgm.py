import json
from sys import argv


def read_index():
    with open('index.json', 'r', encoding='utf-8') as f:
        return json.loads(f.readline())


def read_partition(partition):
    with open(f'{partition}.json', 'r', encoding='utf-8') as f:
        for line in f:
            yield json.loads(line)


def main():
    # with open('partition00.json', 'r', encoding='utf-8') as f:
    #     a = json.loads(f.readline())
    #     print(a['actor']['display_login'])
    #     print(a['repo']['name'])

    flag = 1
    while flag:
        try:
            query = int(input('Please type the number corresponding to the action you would like to do:\n'
                              '\t1. Provide an event ID to find details\n'
                              '\t2. Provide a range of event IDs (inclusive) to find details\n'
                              '\t3. Count data of all event types\n'
                              '\t4. Provide an actor login name to find repositories they have interacted with\n'
                              '\t5. Provide a short name of a repository to find all actors who have interacted with '
                              'the repository\n'
                              '\t6. Quit\n'))
            if query == 1:
                event_id = input('Please input an event ID: ')
                find_event(event_id)
            elif query == 2:
                event_id1 = input('Please input a starting event ID: ')
                event_id2 = input('Please input an ending event ID: ')
                find_event_range(event_id1, event_id2)
            elif query == 3:
                pass
            elif query == 4:
                pass
            elif query == 5:
                pass
            elif query == 6:
                print('Closing Program.')
                flag = 0
            else:
                print("\n\nPlease enter a valid number.\n\n")
        except ValueError:
            print("\n\nPlease enter valid number(s).\n\n")


def find_event(ID):
    flag = 1
    partition_structure = read_index()
    for key, values in zip(partition_structure.keys(), partition_structure.values()):
        if int(values['first_id']) <= int(ID) <= int(values['last_id']):
            for i, line in enumerate(read_partition(key)):
                if line['id'] == ID:
                    flag = 0
                    print()
                    print(json.dumps(line, indent=4))
                    print()
                    print(f'Partitioned files accessed: 1\n'
                          f'Lines inspected: {i + 1}')
                    print('\n\n')
    if flag:
        print('\n\nEvent ID not found.\n'
              'Partitioned files accessed: 0\n'
              'Lines inspected: 0\n\n')


def find_event_range(ID1, ID2):
    flag = 1
    file_cnt = 0
    line_cnt = 0
    partition_structure = read_index()
    for key, values in zip(partition_structure.keys(), partition_structure.values()):
        if int(ID1) <= int(values['first_id']) <= int(ID2) or int(ID1) <= int(values['last_id']) <= int(ID2):
            file_cnt += 1
            for i, line in enumerate(read_partition(key)):
                line_cnt += 1
                if (int(line['id']) >= int(ID1))\
                        and (int(line['id']) <= int(ID2)):
                    flag = 0
                    print()
                    print(json.dumps(line, indent=4))
                    print()

    if flag:
        print('\n\nNo event IDs found.\n'
              f'Partitioned files accessed: {file_cnt}\n'
              f'Lines inspected: {line_cnt}')
        if int(ID1) > int(ID2):
            print('\nCheck to make sure the event ID1 <= event ID2!')
        print('\n\n')
    else:
        print(f'\n\nPartitioned files accessed: {file_cnt}\n'
              f'Lines inspected: {line_cnt}\n\n')


if __name__ == '__main__':
    main()
