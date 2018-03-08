FALSE_STRINGS = ('0', 'F', 'FALSE', 'N', 'NO')


def to_bool(value):
    if value is None or value == '':
        return None
    if isinstance(value, basestring) and value.upper() in FALSE_STRINGS:
        return False
    return bool(value)

