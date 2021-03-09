
def merge_intervals(intervals):
    m_intervals = [intervals[0]]
    for i in range(len(intervals)):
        is_i = False
        j = 0
        while j < len(m_intervals):
            a = intervals[i]
            b = m_intervals[j]
            if a[1] >= b[0] and a[0] <= b[0]:
                b[0] = a[0]
                b[1] = max(b[1], a[1])
                is_i = True
                # break
            elif b[1] >= a[0] and b[0] <= a[0]:
                b[1] = max(b[1], a[1])
                is_i = True
                # break
            j += 1
        if not is_i:
            m_intervals.append(intervals[i])
    print(m_intervals)
    d = {}
    for item in m_intervals:
        d[item]

    return list(set(m_intervals))


if __name__ == '__main__':

    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 1]]) == [[1, 1]]
    assert merge_intervals([[1, 1], [2, 2]]) == [[1, 1], [2, 2]]
    assert merge_intervals([[2, 6], [1, 3]]) == [[1, 6]]
    assert merge_intervals([[2, 6], [3, 5]]) == [[2, 6]]
    assert merge_intervals([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
    print("very good!")
