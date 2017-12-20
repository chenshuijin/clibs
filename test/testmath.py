#!/usr/local/bin/python3
from ctypes import *
import sys

loader = cdll.LoadLibrary
lib = loader("../bin/math.so")

def testadd():
    successCount = 0
    failCount = 0
    dm=[
        ("1", "3", 10),
        ("1212323232323", "1222323232323", 10),
        ("1212323232323", "1222323232323", 10),
        ("1212323232323", "1222323232323", 10),
        ("1212323232323", "1222323232323", 10),
        ("9", "122232323288848848484848484848484848484848323", 10),
        ("9", "0999", 10),
        ("101", "39", 10),
        ("12123232aaaaa32323", "1222323232aaaaaaaffffff323", 16),
        ("323232323aaabcdefaaaaaaaaaaaaaaaaaeeeeeeeeee12123232aaaaa32323", "1222323232aaaaaaaffffff323", 16),
        ("ffffffffffffffffffffffffffffffffffffffffffffff12123232aaaaa32323", "0000000000000000000000000000000aaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbcccccccccccdddddddddddddddddeeeeeeeeeeeeeeeffffffffffffff1222323232aaaaaaaffffff323", 16),
        ("0000000000000000000000000000000000000000000000000000012123232aaaaa32323", "1222323232aaaaaaaffffff323fffffffffffffffffffffffffffffffffffffffffffffffffff", 16),
        ("00000000000000000000000000000000000000000000000000000", "00000000", 16),
        ("ffffffffffffffffffffff12123232aaaaa32323", "1222323232aaaaaaaffffff323fffffffffffffffffffffffffffffffffffffffffffffffffff", 16),
        ("ffffffffffffffffff", "ffffffffffffffff", 16),
        ("fffff", "fffff", 16),
        ("f", "f", 16),
        ("fff", "fff", 16),
        ("f", "ff", 16),
        ("0f", "ff", 16),
        ("0", "ff", 16),
        ("0000", "000000", 8),
        ("0001", "1234567", 8),
        ("7777777777777777777777777777777777777777777777", "1234567", 8),
        ("777777777777777777777", "00000", 8),
        ("777777777777777777777777777777777", "7777777777777777777777", 8),
        ("7777777777777777777777777777777777777777777777777777", "777777777777777", 8),
        ("00000", "77777777777", 8),

    ]

    lib.add.restype = c_char_p
    for i in dm:
        expectret =int(i[0], i[2]) + int(i[1], i[2])
        l=c_char_p(str.encode(i[0]))
        r=c_char_p(str.encode(i[1]))
        base=c_int(i[2])
        ret=int(lib.add(l, r, base).decode(), i[2])
        if ret == expectret:
            successCount += 1
        else:
            failCount += 1
            print("Failed at:",i)
            print("ret:",ret)
            print("ert:", expectret)

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)

def testmul():
    successCount = 0
    failCount = 0
#    '''
    dm=[
        ("1", "3", 10),
        ("1212323232323", "1222323232323", 10),
        ("1212323232323", "1222323232323", 10),
        ("1212323232323", "1222323232323", 10),
        ("1212323232323", "1222323232323", 10),
        ("9", "122232323288848848484848484848484848484848323", 10),
        ("9", "0999", 10),
        ("101", "39", 10),
        ("12123232aaaaa32323", "1222323232aaaaaaaffffff323", 16),
        ("323232323aaabcdefaaaaaaaaaaaaaaaaaeeeeeeeeee12123232aaaaa32323", "1222323232aaaaaaaffffff323", 16),
        ("ffffffffffffffffffffffffffffffffffffffffffffff12123232aaaaa32323", "0000000000000000000000000000000aaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbcccccccccccdddddddddddddddddeeeeeeeeeeeeeeeffffffffffffff1222323232aaaaaaaffffff323", 16),
        ("0000000000000000000000000000000000000000000000000000012123232aaaaa32323", "1222323232aaaaaaaffffff323fffffffffffffffffffffffffffffffffffffffffffffffffff", 16),
        ("00000000000000000000000000000000000000000000000000000", "00000000", 16),
        ("ffffffffffffffffffffff12123232aaaaa32323", "1222323232aaaaaaaffffff323fffffffffffffffffffffffffffffffffffffffffffffffffff", 16),
        ("ffffffffffffffffff", "ffffffffffffffff", 16),
        ("fffff", "fffff", 16),
        ("f", "f", 16),
        ("fff", "fff", 16),
        ("f", "ff", 16),
        ("0f", "ff", 16),
        ("0", "ff", 16),
        ("0000", "000000", 8),
        ("0001", "1234567", 8),
        ("7777777777777777777777777777777777777777777777", "1234567", 8),
        ("777777777777777777777", "00000", 8),
        ("777777777777777777777777777777777", "7777777777777777777777", 8),
        ("7777777777777777777777777777777777777777777777777777", "777777777777777", 8),
        ("00000", "77777777777", 8),

    ]
#    '''
#    dm = [("1", "3", 10)]
    lib.mul.restype = c_char_p
    for i in dm:
        expectret =int(i[0], i[2]) * int(i[1], i[2])
        l=c_char_p(str.encode(i[0]))
        r=c_char_p(str.encode(i[1]))
        base=c_int(i[2])
        ret=int(lib.mul(l, r, base).decode(), i[2])
        if ret == expectret:
            successCount += 1
        else:
            failCount += 1
            print(sys._getframe().f_code.co_name," Failed at:",i)
            print("ret:",ret)
            print("ert:", expectret)

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)


testadd()
testmul()
