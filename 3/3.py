#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main():
    question = raw_input()

    pattern = r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]"
    print "".join(i for i in re.findall(pattern, question))


if __name__ == '__main__':
    main()

