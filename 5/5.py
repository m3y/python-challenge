#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import pickle


def main():
    banner = "http://www.pythonchallenge.com/pc/def/banner.p"

    data = pickle.load(urllib.urlopen(banner))
    for i in data:
        print "".join(k*v for k,v in i)


if __name__ == '__main__':
    main()
