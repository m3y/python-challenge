#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib


def main():
    base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    code = input()

    while True:
        data = urllib.urlopen(base + str(code)).read()
        next_code = data.split(" ")[-1]
        try:
            int(str(next_code))
            code = next_code
        except ValueError:
            print code + ": " + data
            break


if __name__ == '__main__':
    main()
