import os
import sys
import math


def slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k +1) / (2 * k + 1)
    return s


def pi(n):
    childs = {}
    unit = n / 10
    for i in range(10):
        mink = unit * i
        maxk = mink + unit
        r, w = os.pipe()
        pid = os.fork()
        if pid > 0:
            childs[pid] = r
            os.close(w)
        else:
            os.close(r)
            s = slice(mink, maxk)
            os.write(w, str(s))
            sys.exit(0)
    sums = []
    for pid, r in childs.items():
        sums.append(float(os.read(r, 1024)))
        os.close(r)
        os.waitpid(pid, 0)
    return math.sqrt(sum(sums) * 8)

print pi(10000000)