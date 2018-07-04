# -*- coding: utf-8 -*-
import sys


class Hanoi:
    def move(self, a, b, c, n):
        if n == 1:
            c.append(a[len(a) - 1])
            del a[len(a) - 1]
            if f == 1:
                self.display(a, b, c)
        else:
            self.move(a, c, b, n - 1)
            c.append(a[len(a) - 1])
            del a[len(a) - 1]
            if f == 1:    self.display(a, b, c)
            self.move(b, a, c, n - 1)

    def __init__(self, n):
        if n > 0:
            self.a = []
            for i in range(n):
                self.a.append(n - i)
            self.b = []
            self.c = []
            self.n = n
            self.display(self.a, self.b, self.c)
            self.move(self.a, self.b, self.c, self.n)

    def display(self, a, b, c):
        print
        u"1: ",
        for i in range(len(a)):
            print
            str(a[i]) + ' ',
        print
        ""
        print
        u"2: ",
        for i in range(len(b)):
            print
            str(b[i]) + ' ',
        printd
        ""
        print
        u"3: ",
        for i in range(len(c)):
            print
            str(c[i]) + ' ',
        print
        ""


if len(sys.argv) > 3 or len(sys.argv) < 2:
    print
    "error"
    sys.exit(1)
f = 0
n = int(sys.argv[1])
if len(sys.argv) == 3 and sys.argv[2] == "-v":
    f = 1

x = Hanoi(n)

del x

sys.exit(u"Complete")