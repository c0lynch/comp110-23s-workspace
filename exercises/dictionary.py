"""IDK, what do you want this to be?"""
__author__ = "730620941"


def invert(di: dict[str, str]) -> dict[str, str]:
    """Fair is foul and foul is fair."""
    d: dict[str, str] = {}
    for key in di:
        if di[key] in d:
            raise KeyError
        d[di[key]] = key
    return d


def favorite_color(c: dict[str, str]) -> str:
    """Returns the most favorite color."""
    lis: list[str] = []
    lis2: dict[str, int] = {}

    for key in c:
        if c[key] in lis2:
            lis2[c[key]] += 1
        else:
            lis2[c[key]] = 1
    for key in lis2:
        if 
        # which is lowerst 
        # if there is a tie, then 


def count(lis: list[str]) -> dict[str, int]:
    """Returns a dictionary of how many times an element in a list is repeated."""
    d: dict[str, int] = {}
    for elem in lis:
        d[elem] = lis.count(elem)
    return d