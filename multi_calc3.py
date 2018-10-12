import os
import sys
import math
import socket

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
        rsock, wsock = socket.socketpair()
        pid = os.fork()
        if pid > 0:
            childs[pid] = rsock
            wsock.close()
        else:
            rsock.close()
            s = slice(mink, maxk)
            wsock.send(str(s))
            wsock.close()
            sys.exit(0)
    sums = []
    for pid, rsock in childs.items():
        sums.append(float(rsock.recv(1024)))
        rsock.close()
        os.waitpid(pid, 0)
    return math.sqrt(sum(sums) * 8)

print pi(10000000)