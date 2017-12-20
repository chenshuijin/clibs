#!/usr/local/bin/python3
from ctypes import *
import sys

loader = cdll.LoadLibrary
lib = loader("../bin/util.so")

def testreverse():
    successCount = 0
    failCount = 0

    dm=["43434fffdsfasf",
        "sdfsadfsdff",
        "dfsadfsdfasdfasdfsdfasdfasdfasdfsdfsdf",
        "r3rednhdfvhfijdsbhnjhjfhikjhuiijuiwu87439",
        "",
        "dfasdfa12323",
        "1111111234567900009876545678765445",
        "0000000000",
        "11111",
        "2222",
        "1a1",
        "22sss"
    ]

    lib.reverse.restype = c_char_p
    for i in dm:
        l=c_char_p(str.encode(i))
        ret=lib.reverse(l)
        if ret.decode()==i[::-1]:
            successCount += 1
        else:
            failCount += 1
            print("Failed at:",i)

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)

def testctoi():
    successCount = 0
    failCount = 0

    dm=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

    lib.ctoi.restype = c_int
    for i in dm:
        c=c_char(str.encode(i))
        ret=lib.ctoi(c)
#        print("testctoi:",ret)
        if ret==int(i,16):
            successCount += 1
        else:
            failCount += 1
            print("Failed at:",i)

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)

def testitoc():
    successCount = 0
    failCount = 0

    dm=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    lib.itoc.restype = c_char
    for i in dm:
        ret=lib.itoc(i, 16)
        if i == int(ret, 16):
            successCount += 1
        else:
            failCount += 1
            print("Failed at:",i)

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)

def testlstrip():
    successCount = 0
    failCount = 0

    dm=["      43434fffdsfasf",
        "sdfsadfsdff      ",
        "dfsadfsdf   asdfasdfsdfasdfasdfasdfsdfsdf",
        "r3rednhdfvhf   ijdsbhnjhjfhikjhuiijuiwu87439",
        "",
        "         ",
        "    dfasdfa12323   ",
        "1111111234567900009876545678765445",
        "0000000000",
        "11111",
        "2222",
        "1a1",
        "22sss          "
    ]

    lib.lstrip.restype = c_char_p
    for i in dm:
        l=c_char_p(str.encode(i))
        c=c_char(str.encode("a"))
        ret=lib.lstrip(l, c)
        if ret.decode() == i.lstrip("a"):
            successCount += 1
        else:
            failCount += 1
            print("Failed at:",i)

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)

def testrpad():
    successCount = 0
    failCount = 0

    dm=[("abcdef", "c", 7),
        ("abcdef", "0", 0),
        ("abcdef", "0", 1),
        ("abcdef", "0", 100),
    ]

    lib.rpad.restype = c_char_p
    for i in dm:
        dest=c_char_p(bytes(i[2]))
        src=c_char_p(str.encode(i[0]))
        c=c_char(str.encode(i[1]))
        len=c_int(i[2])
        ret=lib.rpad(dest, src, c, len)
        if ret.decode() == i[0].ljust(i[2], i[1]):
            successCount += 1
        else:
            failCount += 1
            print("Failed at:",i)
            print("ret:", ret.decode())
            print("expect:", i[0].ljust(i[2], i[1]))

    print(sys._getframe().f_code.co_name,"Passed:",successCount,"Failed:",failCount)

#'''
testreverse()
testctoi()
testitoc()
testlstrip()
#'''
testrpad()
