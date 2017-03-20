#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import zipfile


def main():
    f = zipfile.ZipFile("6.data/channel.zip")
    fileno = "90052"
    comments = []

    while True:
        data = f.read(fileno + ".txt").decode("u8")
        nextno = data.split(" ")[-1]
        try:
            int(str(nextno))
            comments.append(f.getinfo(fileno + ".txt").comment.decode("u8"))
            fileno = nextno
        except ValueError:
            print fileno + ": " + data
            break

    print "".join(comments)


if __name__ == '__main__':
    main()
