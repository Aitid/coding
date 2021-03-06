from collections import defaultdict


def f(nums, target):
    n_d = defaultdict(int)
    for i, v in enumerate(nums):
        n_d[v] = i

    for i, v in enumerate(nums):
        x = target - v
        if x in n_d and n_d[x] != i:  # обязательно проверить что бы он не сослался на себя
            print(i, n_d[x])
            return [i, n_d[x]]


if __name__ == '__main__':

    assert f([2, 7, 11, 15], 9) == [0, 1]
    assert f([3, 2, 4], 6) == [1, 2]
    assert f([3, 3], 6) == [0, 1]
    assert f([1, 3, 4, 5, 1], 2) == [0, 4]
