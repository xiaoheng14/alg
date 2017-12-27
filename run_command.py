# -*- coding: utf-8 -*-
import time
import subprocess


class TimeoutError(Exception):
    pass


def command(cmd, timeout=60):
    """
    执行命令cmd，返回命令输出的内容。
    如果超时将会抛出TimeoutError异常。
    cmd - 要执行的命令
    timeout - 最长等待时间，单位：秒
    """
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    # for i in iter(p.stdout.readline, 'b'):
    #     print i
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            res = []
            for i, v in enumerate(iter(p.stdout.readline, 'b')):
                res.append(v)
                if i > 20:
                    return res
            return res
            # p.terminate()
            # raise TimeoutError(cmd, timeout)
        time.sleep(0.1)
    return p.stdout.read()


def command_limit(cmd, timeout=10, max_lines=10000):
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        if p.poll() is not None:
            break
        result = list()
        for index, value in enumerate(iter(p.stdout.readline, 'b')):
            seconds_passed = time.time() - t_beginning
            result.append(value)
            if (timeout and seconds_passed > timeout) or index > max_lines:
                break
        return result


def save_command(result):
    with open('/root/test.log', 'w') as f:
        for line in result:
            f.write(line)


if __name__ == "__main__":
    c = command_limit(cmd='man top', timeout=10)
    save_command(c)
