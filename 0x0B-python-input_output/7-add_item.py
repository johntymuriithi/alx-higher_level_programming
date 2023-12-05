#!/usr/bin/python3
"""
    this method writes to file
    """


def main():
    """
    this method writes to file
    """

    mod = __import__('sys')
    mod2 = __import__('5-save_to_json_file')
    mod1 = __import__('6-load_from_json_file')
    args = mod.argv[1:]
    mylist = list(args)

    file2 = mod1.load_from_json_file('add_item.json') or []
    file2.extend(mylist)

    mod2.save_to_json_file(file2, 'add_item.json')


if __name__ == "__main__":
    main()
