import os
import sys
import math


def slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k +1) / (2 * k + 1)
    return s


def pi(n):
    pids = []
    unit = n / 10
    for i in range(10):
        mink = unit * i
        maxk = mink + unit
        pid = os.fork()
        if pid > 0:
            pids.append(pid)
        else:
            s = slice(mink, maxk)
            with open("%d" % os.getpid(), 'w') as f:
                f.write(str(s))
            sys.exit(0)
    sums = []
    for pid in pids:
        os.waitpid(pid, 0)
        with open("%d" % pid, 'r') as f:
            sums.append(float(f.read()))
        os.remove("%d" % pid)
    return math.sqrt(sum(sums) * 8)

print pi(10000000)