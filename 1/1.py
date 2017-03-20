#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

QUESTION="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
QUESTION2="map"

def main():
    trans = string.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'cdefghijklmnopqrstuvwxyzab')

    print QUESTION.translate(trans)
    print QUESTION2.translate(trans)


if __name__ == '__main__':
    main()

