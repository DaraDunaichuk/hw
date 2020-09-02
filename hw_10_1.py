import json
import sys
import re


def update_key(val, key):

    if key == 'name':

        rev = ''.join([elem for elem in reversed(val)])
        try:
            pos = rev.index(' ')
            pos = len(val) - pos
        except:
            pos = 0
        return val[pos:]
    elif key == 'years':

        year = re.findall(r'\d{1,}', val)

        bc = re.findall(r'BC', val)

        return int(year[1]) * (1 if len(bc) == 0 else -1)
    elif key == 'text':

        words = re.findall(r'\w{1,}', val)
        return (len(words))
    else:
        raise ValueError('No such key for sort')


def json_sort(my_list, key):

    sort_dict = {}
    for item in my_list:
        value = item[key]
        sort_dict.update({update_key(value, key): item})
    sequence = list(sort_dict.keys())
    sequence.sort()
    return sequence, [sort_dict[item] for item in sequence]


def main(file):

    with open(file, 'r') as f:
        writers = json.load(f)
        f.close()
    for sort_type in ['name', 'years', 'text']:
        print('Тип сортировки: ' + sort_type)
        seq, lst = json_sort(writers, sort_type)
        print('Сортировка ключей')
        print(seq)
        print('---------------')
        print('Сортировка JSON')
        print(lst)
        print('\n')

my_sorted_list = main("math_.json")
print(my_sorted_list)

