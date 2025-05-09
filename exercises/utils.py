"""EX05 - `list` Utility Functions."""
__author__ = "730620941"


def only_evens(c: list[int]) -> list[int]:
    """Makes a list of only evens from the list."""
    x: int = 0
    f: list[int] = []
    while x <= (len(c) - 1):
        if c[x] % 2 == 0:
            f.append(c[x])
        x += 1
    return f


def concat(m1: list[int], m2: list[int]) -> list[int]:
    """Takes 2 lists to make one."""
    lm: list[int] = []
    for elem in range(0, len(m1)):
        lm.append(m1[elem])
    for elem in range(0, len(m2)):
        lm.append(m2[elem])
    return lm


def sub(alist: list[int], sr: int, er: int) -> list[int]:
    """pulls items from the list given the index number."""
    x: list[int] = []
    if len(alist) == 0 or sr >= len(alist) or er <= 0:
        return x
    else:
        for elem in range(sr, (er)):
            x.append(alist[elem])
        return x