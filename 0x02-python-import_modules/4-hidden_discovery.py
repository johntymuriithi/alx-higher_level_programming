#!/usr/bin/python3
if __name__ == "__main__":
    import importlib

    module = importlib.import_module('hidden_4')
    names = dir(module)

    for i, en in enumerate(names):
        if en[0] == '_':
            continue
        print(f"{en}")
