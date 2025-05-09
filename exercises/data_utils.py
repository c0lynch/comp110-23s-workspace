from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a speific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column header as keys"""
    result: dict[str, list[str]] = {}
    first_row: dict[str,str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result

    
def head(d: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    em: dict[str, list[str]] = {}
    for key in d:
        l: list[str] = []
        for elem in range(0,n):
            l.append(d[key][elem])
        em[key] = l
    return em

def select(d: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    new: dict[str, list[str]] = {}
    for key in d:
        if key in names:
            new[key] = d[key]
    return new
    
def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    c: dict[str, list[str]] = {}
    l: list[str] = []
    for key in a:
        l.append(key)
    
def count(a: list[str]) -> dict[str, int]:
    new: dict[str, list[int]] = {}
    for elem in a:
        if elem in new:
            new[elem] += 1
        else:
            new[elem] = 0
    return new


