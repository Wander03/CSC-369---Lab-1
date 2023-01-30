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
                type_summary()
            elif query == 4:
                actor = input('Please input an actor name: ')
                find_repos(actor)
            elif query == 5:
                repo = input('Please input a repository name: ')
                find_actors(repo)
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
            for line in read_partition(key):
                line_cnt += 1
                if (int(line['id']) >= int(ID1)) \
                        and (int(line['id']) <= int(ID2)):
                    flag = 0
                    print()
                    print(json.dumps(line, indent=4))
                    print()
                else:
                    break

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


def type_summary():
    types = {}
    file_cnt = 0
    line_cnt = 0
    partition_structure = read_index()
    for key in partition_structure.keys():
        file_cnt += 1
        for line in read_partition(key):
            line_cnt += 1
            event_type = line['type']
            if event_type not in types.keys():
                types[event_type] = 1
            else:
                types[event_type] += 1

    type_cnt = []
    for t, n in zip(types.keys(), types.values()):
        type_cnt.append([t, n])

    type_cnt.sort(key=lambda x: x[1], reverse=True)

    print()
    for t in type_cnt:
        print(f'{t[0]}: {t[1]}')
    print(f'\nPartitioned files accessed: {file_cnt}\n'
          f'Lines inspected: {line_cnt}\n\n')


def find_repos(name):
    repo_set = set()
    file_cnt = 0
    line_cnt = 0
    partition_structure = read_index()
    for key in partition_structure.keys():
        file_cnt += 1
        for line in read_partition(key):
            line_cnt += 1
            if name == line['actor']['display_login']:
                repo_set.add(line['repo']['name'])

    print()
    if not repo_set:
        print(f'"{name}" has not interacted with any repositories.')
    else:
        for repo in repo_set:
            print(repo)

    print(f'\nPartitioned files accessed: {file_cnt}\n'
          f'Lines inspected: {line_cnt}\n\n')


def find_actors(repo):
    actors_set = set()
    file_cnt = 0
    line_cnt = 0
    partition_structure = read_index()
    for key in partition_structure.keys():
        file_cnt += 1
        for line in read_partition(key):
            line_cnt += 1
            if repo == line['repo']['name']:
                actors_set.add(line['actor']['display_login'])

    print()
    if not actors_set:
        print(f'"{repo}" has not had any actors interact with it.')
    else:
        for actor in actors_set:
            print(actor)

    print(f'\nPartitioned files accessed: {file_cnt}\n'
          f'Lines inspected: {line_cnt}\n\n')


if __name__ == '__main__':
    main()
