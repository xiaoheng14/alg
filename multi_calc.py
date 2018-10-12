import os
import sys
import math
import redis


def slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k +1) / (2 * k + 1)
    return s

def pi(n):
    pids = []
    unit = n / 10
    client = redis.StrictRedis()
    client.delete('result')
    del client

    for i in range(10):
        mink = unit * i
        maxk = mink + unit
        pid = os.fork()
        if pid > 0:
            pids.append(pid)
        else:
            s = slice(mink, maxk)
            client = redis.StrictRedis()
            client.rpush("result", str(s))
            sys.exit(0)
    for pid in pids:
        os.waitpid(pid, 0)
    sum = 0
    client = redis.StrictRedis()
    for s in client.lrange("result", 0, -1):
        sum += float(s)
    return math.sqrt(sum * 8)

print pi(10000000)