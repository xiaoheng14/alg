# -*- coding: utf-8 -*-
import os

FALSE_STRINGS = ('0', 'F', 'FALSE', 'N', 'NO')


def to_bool(value):
    if value is None or value == '':
        return None
    if isinstance(value, basestring) and value.upper() in FALSE_STRINGS:
        return False
    return bool(value)


def get_mac_addresses():
    addresses = []
    sys_class_net = "/sys/class/net"
    interfaces = os.walk(sys_class_net)
    for root, ifaces, files in os.walk(sys_class_net):
        for iface in ifaces:
            if iface == "lo": # skip loopback
                continue
            addr_file = os.path.join(sys_class_net, iface, "address")
            addresses.append(open(addr_file, 'rb').read())
        break
    return sorted(addresses)


def get_computer_id():
    try:
        with open('/var/lib/dbus/machine-id', 'rb') as f:
            cid = f.read()
    except IOError:
        cid = get_mac_addresses()
    return cid

from pwd import getpwnam
print getpwnam('ub')