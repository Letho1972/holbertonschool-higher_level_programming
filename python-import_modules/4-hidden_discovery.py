#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hide_mod = dir(hidden_4)

    for name in hide_mod:
        if not name.startswith('__'):
            print("{}".format(name))
