"""EX04 - `list` Utility Functions."""
__author__ = "730620941"


def all(lad: list[int], num: int) -> bool:
    x: int = 0
    al: bool = True
    if len(lad) == 0:
        al = False
    while x < len(lad) and al:
        if lad[x] == num:
            x = x + 1
        else:
            al = False
    return al
    
    
def max(c: list[int]) -> int:
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")
    z: int = 0
    y: int = (len(c) - 1)
    m: int = c[0]
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")
    while z <= y:
        if m < c[z]:
            m = c[z]
        z += 1
    return m
    
    
def is_equal(l1: list[int], l2: list[int]) -> bool:
    v: int = 0
    w: bool = True
    x: int = len(l1)
    if len(l1) == 0 and len(l2) == 0:
        raise ValueError("is_equal() arg is an empty List")
    while v < x:
        if l1[v] != l2[v]:
            w = False
        v += 1
    return w