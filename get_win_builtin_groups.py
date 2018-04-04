# -*- coding: utf-8 -*-
import re
import os

def run_shell_result(command):
    return os.popen(command).read()
    
def get_builtin_groups():
    builtin_group = list()
    result = run_shell_result("wmic group list full")
    try:
        for res in (re.split('[\r\n]{3,}', result.strip())):
            try:
                if not res:
                    continue
                name = None
                sid = None
                for r in res.split('\r\n'):
                    if not r:
                        continue
                    match_name = re.match('Name=(.*)', r)
                    match_sid = re.match('SID=(.*)', r)
                    if match_name:
                        name = match_name.group(1)
                    elif match_sid:
                        sid = match_sid.group(1).strip()
                        if not sid.startswith('S-1-5-32-'):
                            sid = None
                if not name or not sid:
                    continue
                builtin_group.append(name)
            except Exception as e:
                print e
    except Exception as e:
        print e
    return builtin_group
