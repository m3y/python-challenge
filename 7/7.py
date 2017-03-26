#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

import urllib
import re


def main():
    data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
    img = Image.open(data, "r")
    pixels = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
    answer = [r for r, g, b, a in pixels if r == g == b][::7]
    print "".join(map(chr, answer))
    answer2 = re.findall("\d+", "".join(map(chr,answer)));
    print "".join(map(chr, map(int, answer2)))


if __name__ == '__main__':
    main()

