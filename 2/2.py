#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

def main():
    question = raw_input()

    d = OrderedDict()
    for i in question:
        if i in d.keys():
            d[i]+=1
        else:
            d[i] = 1

    print "".join(k for k,v in d.items() if v==1)


if __name__ == '__main__':
    main()

