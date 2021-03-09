
from collections import defaultdict


def mapping():
    d = {}
    for i in range(97, 97 + 26):
        d[i] = chr(i).upper()
    return d


def is_valid(nums):
    for i in nums:
        if int(i) > 26:
            return False
        elif i[0] == '0':
            return False
    return True


def f(s):
    counter = 0
    if is_valid(list(s)):
        counter += 1

    for i in range(len(s)-1):
        nums = []
        nums += s[0:i]
        nums.append(s[i:i+2])
        nums += s[i+2:]
        print(nums)
        if is_valid(nums):
            counter += 1
    return counter


if __name__ == '__main__':

    # assert f("12") == 2
    # assert f("226") == 3
    # assert f("2206") == 1
    # assert f("0206") == 0
    # assert f("0") == 0
    assert f("1020") == 1
    # assert f("01") == 0
    # assert f("010") == 0
    # assert f("1717") == 3
    # assert f("7777") == 1

