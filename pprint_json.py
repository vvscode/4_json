import json
import sys


def load_data(filepath):
    with open(filepath) as filepointer:
        return filepointer.read()


def pretty_print_json(string):
    json_data = json.loads(string)
    print(json.dumps(json_data, sort_keys=True, indent=4))


def main():
    if len(sys.argv) != 2:
        print('You have to pass filename as an argument')
    else:
        try:
            pretty_print_json(load_data(sys.argv[1]))
        except FileNotFoundError:
            print('Please use correct file name')
        except json.JSONDecodeError:
            print("Not a correct json")


if __name__ == '__main__':
    main()
