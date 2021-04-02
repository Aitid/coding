def read_n(p, n):

    s, i = [], 1
    for line in open(p):
        s.append(line)
        if i == n:
            yield ''.join(s)
            s, i = [], 1
        else:
            i += 1
    if s:
        yield ''.join(s)


if __name__ == '__main__':
    f = 'filename.txt'
    gen = read_n(f, 1)
