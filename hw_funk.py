import os, sys, json, csv,string
import random as rn

sym_range = (33, 100)
az_range = (97, 122)
chars = string.ascii_letters+string.digits+string.punctuation

def gen_string(len_, symbols):
    a, b = symbols
    result = [chr(rn.randint(a, b)) for val in range(len_)]
    return ''.join(result)


def write_txt(file):
    len_string = rn.randint(100, 1000)
    to_write = gen_string(len_string, sym_range) + '\n' * 9
    with open(file, 'w') as txt_file:
        txt_file.write(to_write)
        txt_file.close()


def write_json(file):
    res = {}
    for i in range(rn.randint(5, 21)):
        value = [rn.randint(-100, 100)]
        value.extend([rn.random()])
        value.extend([rn.choice([True, False])])
        res.update({gen_string(5, az_range): rn.choice(value)})
    with open(file, 'w') as json_file:
        json_file.write(json.dumps(res))


def write_csv(file):
    m = rn.randint(3, 10)
    n = rn.randint(3, 10)
    list_n = []
    for i in range(n):
        list_n.append([rn.choice([0, 1]) for j in range(m)])
    with open(file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for row in list_n:
            writer.writerow(row)


def main(file):
    filename, file_extension = os.path.splitext(file)
    if file_extension[1:] == 'txt': write_txt(file)
    elif file_extension[1:] == 'json': write_json(file)
    elif file_extension[1:] == 'csv': write_csv(file)
    else:
        print('Unsupported file format')
        exit(1)

something = main("hw.txt")


