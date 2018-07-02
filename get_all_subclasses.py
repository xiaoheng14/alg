# -*- coding: utf-8 -*-
class Base(object):
    def __init__(self):
        self.name = 'base'
        
class A(Base):
    def __init__(self):
        super(A, self).__init__()
        self.value = 'A'
class B(Base):
    def __init__(self):
        super(B, self).__init__()
        self.value = 'B'

class C(A):
    def __init__(self):
        super(C, self).__init__()
        self.value = 'C'
    

a = A()
print isinstance(a, Base)
b = B()
print isinstance(b, Base)
c = C()
print isinstance(c, Base)


def get_all_sub_objects(base, result=None):
    if not isinstance(result, dict):
        result = dict()
    for subclass in base.__subclasses__():
        if not subclass.__name__ in result:
            result[subclass.__name__] = subclass
        get_all_sub_objects(subclass, result)
    return result

print get_all_sub_objects(Base)

def get_all_sub_objects2(base):
    if not isinstance(base, type):
        raise TypeError('need new-style class')
    try:
        subs = base.__subclasses__()
    except TypeError:
        subs = cls.__subclassed__(cls)
    for sub in subs:
        yield sub
        for sub in get_all_sub_objects2(sub):
            yield sub

for sub in get_all_sub_objects2(Base):
    print sub
