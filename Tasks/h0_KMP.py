from typing import Optional, List


def _substr(prefix_str):
    for i in range(2, len(prefix_str)):
        yield prefix_str[:i]
    yield prefix_str


def _pref(prefix_str):
    for i in range(1, len(prefix_str)):
        yield prefix_str[:i]


def _suf(prefix_str):
    for i in range(1, len(prefix_str)):
        yield prefix_str[-i:]


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    prefix_list = [0]
    for substr in _substr(prefix_str):
        max_leight = 0
        for pref, suf in zip(_pref(substr), _suf(substr)):
            if pref == suf:
                max_leight = len(pref)
        prefix_list.append(max_leight)

    return prefix_list


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    prefix_fun = _prefix_fun(substr)
    i = 0
    j = 0
    while i < len(inp_string):
        if inp_string[i] == substr[j]:
            i += 1
            j += 1
            if j == len(substr):
                return i - len(substr)
        else:
            if j == 0:
                i += 1
            else:
                j = prefix_fun[j - 1]



def main():
    _str = "abcabcd"
    _prefix_fun(_str)
    print(kmp_algo("abcabcabcd", _str))


if __name__ == '__main__':
    main()