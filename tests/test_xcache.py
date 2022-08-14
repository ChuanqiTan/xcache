# -*- coding: utf-8 -*-

"""
Authors:
    chuanqi.tan ### gmail.com

XCache: A simple and thread-safe LRU cache, which support key-func, release-func and hit-stat.

Features:
    - LRU cache
    - Thread safe
    - Support special key function
    - Support special release function
    - Has detail hit stat
"""

import json
from xcache import xcache, show_xcache_hit_stat


@xcache(3)
def calc1(x, y):
    print("calc1 {}, {}".format(x, y))
    return x + y


@xcache(3, key_func=lambda x,y: (x, y), log_keys=True)
def calc2(x, y):
    print("calc2 {}, {}".format(x, y))
    return x + y


def _release(x):
    del x


if __name__ == "__main__":
    x=calc2
    print(x(5, 6))
    print(x(5, 6))
    print(x(5, 6))
    print(x(5, 5))
    print(x(4, 6))
    print(x(3, 6))
    print(x(2, 6))
    print(x(1, 6))
    print(x(9, 6))
    print(json.dumps(show_xcache_hit_stat(x), indent=4))
    print(x.__xcache__._hit_detail)
    print(x.__xcache__._key_detail)
