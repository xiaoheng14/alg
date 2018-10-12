import os
import sys
import math
from posix_ipc import MessageQueue as Queue

def slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k +1) / (2 * k + 1)
    return s


def pi(n):
    pids = []
    unit = n / 10
    q = Queue("/pi", flags=os.O_CREAT)
    for i in range(10):
        mink = unit * i
        maxk = mink + unit
        pid = os.fork()
        if pid > 0:
            pids.append(pid)
        else:
            s = slice(mink, maxk)
            q.send(str(s))
            q.close()
            sys.exit(0)
    sums = []
    for pid in pids:
        sums.append(float(q.receive()[0]))
        os.waitpid(pid, 0)
    q.close()
    q.unlink()
    return math.sqrt(sum(sums) * 8)

print pi(10000000)