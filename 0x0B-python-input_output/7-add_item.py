#!/usr/bin/python3


def main():
    """
    this method writes to file
    """

    sys = __import__('sys')
    jsonn = __import__('json')
    save_to_json_file = __import__('5-save_to_json_file')
    load_from_json_file = __import__('6-load_from_json_file')
    with open("add_item.json", "a+", encoding="UTF8") as file:
        file.seek(0)
        list_in_file = file.read()

        if list_in_file:
            list_in_file = jsonn.loads(list_in_file)

    if type(list_in_file) != list:
        list_in_file = []

    for x in range(len(sys.argv)):
        if x != 0:
            list_in_file.append(sys.argv[x])

    with open("add_item.json", "w", encoding="UTF8") as file:
        file.write(jsonn.dumps(list_in_file))

if __name__ == "__main__":
    main()
