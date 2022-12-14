XCache: A simple and thread-safe LRU cache, which support key-func, release-func and hit-stat.
===============

Setup
===============
```bash
pip install xcache-lib
```


Key Features
===============
- LRU cache
- Thread safe
- Support special key function
- Support special release function
- Has detail hit stat


Core Function Descriptor: xcache
================

```python
@xcache(cache_size, key_func=None, release_func=None, log_keys=False)
```

| Param Value  | Description                 |
| ------------ | ----------------------------|
| cache_size   | size of cache storage       |
| key_func     | special key function        |
| release_func | special release function    |
| log_keys     | log keys, for ``DEBUG``     |


Quick Start
===============

```python
from xcache import xcache, show_xcache_hit_stat


@xcache(3, key_func=lambda x,y: x, log_keys=True)
def calc(x, y):
    print("calc {}, {}".format(x, y))
    return x + y


if __name__ == "__main__":
    print(calc(5, 6))
    print(calc(5, 6))
    print(calc(5, 6))
    print(calc(5, 5))
    print(calc(4, 6))
    print(calc(3, 6))
    print(calc(2, 6))
    print(calc(1, 6))
    print(calc(9, 6))

    print(json.dumps(show_xcache_hit_stat(calc), indent=4))  # show detail hit stat
```

outputs:

```bash
calc 5, 6
11
11
11
calc 5, 5
10
calc 4, 6
10
calc 3, 6
9
calc 2, 6
8
calc 1, 6
7
calc 9, 6
15
{
    "hit_rate": 22.22222222222222, 
    "dup_calc_rate": 0.6666666666666666, 
    "hit": [
        2, 
        7
    ], 
    "keys_num": 1, 
    "detail": {
        "key_detail": {
            "1": 6, 
            "3": 1
        }, 
        "hit_detail": {
            "2": 1
        }
    }
}
```
