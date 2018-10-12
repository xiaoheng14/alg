import os
import sys
import math
import struct
import posix_ipc
from posix_ipc import Semaphore
from posix_ipc import SharedMemory as Memory


def slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k +1) / (2 * k + 1)
    return s

def pi(n):
    pids = []
    unit = n / 10
    sem_lock = Semaphore("/pi_sem_lock", flags=posix_ipc.O_CREX, initial_value=1)
    memory = Memory("/pi_rw", size=8, flags=posix_ipc.O_CREX)
    os.lseek(memory.fd, 0, os.SEEK_SET)
    os.write(memory.fd, struct.pack('d', 0.0))
    for i in range(10):
        mink = unit * i
        maxk = mink + unit
        pid = os.fork()
        if pid > 0:
            pids.append(pid)
        else:
            s = slice(mink, maxk)
            sem_lock.acquire()
            try:
                os.lseek(memory.fd, 0, os.SEEK_SET)
                bs = os.read(memory.fd, 8)
                cur_val, = struct.unpack('d', bs)
                cur_val += s
                bs = struct.pack('d', cur_val)
                os.lseek(memory.fd, 0, os.SEEK_SET)
                os.write(memory.fd, bs)
                memory.close_fd()
            finally:
                sem_lock.release()
            sys.exit(0)
    sums = []
    for pid in pids:
        os.waitpid(pid, 0)
    os.lseek(memory.fd, 0, os.SEEK_SET)
    bs = os.read(memory.fd, 8)
    sums, = struct.unpack('d', bs)
    memory.close_fd()
    memory.unlink()
    sem_lock.unlink()
    return math.sqrt(sums * 8)

print pi(10000000)