import json
import sys


def load_data(filepath):
    file_pointer = open(filepath, 'r')
    file_content = file_pointer.read()
    file_pointer.close()
    return file_content


def pretty_print_json(string):
    try:
        json_data = json.loads(string)
        print(json.dumps(json_data, sort_keys=True, indent=4))
    except:
        print(string)


def main(file_path):
    pretty_print_json(load_data(file_path))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('You have to pass filename as an argument')
    else:
        main(sys.argv[1])
