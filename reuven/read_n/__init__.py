"""
Welcome to the first sample exercise!  If you subscribe to Weekly Python Exercise, you'll get a new exercise like this one sent to you automatically every Tuesday.  Moreover, you'll have exclusive access to our forums and discussion.

Normally, if we want to read from a file in Python, we do so one line at a time, as follows:

    for one_line in open(filename):
        print(one_line.rstrip())


But sometimes, we want to read more than one line at a time.

For example, suppose a logfile is written in a three-line format. Reading one line at a time is pretty useless, especially if we want to compare a value on line 1 with a value on line 3.

Reading the entire file into a string isn't what we want, either; it might well be too long for us to read the entire thing.  What I really want to do is read three lines at a time.

For this exercise, I want you to write a generator function that takes two arguments — the filename from which to read, and the maximum number of lines that should be returned with each iteration.  That is, if our file is

    File line 0 aaa
    File line 1 bbb
    File line 2 ccc
    File line 3 ddd
    File line 4 eee
    File line 5 fff
    File line 6 ggg


Then I could do this:

    for two_lines in read_n(filename, 2):
        print(two_lines.rstrip())


And the result would be:

   File line 0 aaa
   File line 1 bbb

   File line 2 ccc
   File line 3 ddd

   File line 4 eee
   File line 5 fff

   File line 6 ggg


Notice that the last line is by itself, because there was an odd number of lines.  We could also say:

    for four_lines in read_n(filename, 4):
        print(four_lines.rstrip())


This time we get four lines at a time:

   File line 0 aaa
   File line 1 bbb
   File line 2 ccc
   File line 3 ddd

   File line 4 eee
   File line 5 fff
   File line 6 ggg


With each iteration, read_n should return a string (not a list) containing up to the number of lines specified by the second parameter.

Note that read_n isn't a function that returns a list, but rather a generator function.  In other words, executing read_n will return a generator object -- in other words, an object that implements Python's iteration protocol, and thus knows how to behave inside of a "for" loop or list comprehension.

If you're not sure how to write a generator function, here is some good online documentation here:

    https://realpython.com/blog/python/introduction-to-python-generators/

I'll be back tomorrow with a solution.  The test file (for use with "pytest") is below.  It assumes that the solution is in a file called "solution.py".

Reuven
```

import pytest

from solution import read_n
from io import StringIO
from string import ascii_lowercase

filename = 'alphabet.txt'

def create_alphabet_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / filename

    text = '\n'.join(f'{one_letter*20}'
                     for one_letter in ascii_lowercase) + '\n'
    p.write_text(text)
    return p

@pytest.mark.parametrize('n,expected', [
    (1, 26),
    (2, 13),
    (3, 9),
    (4, 7)])
def test_read_n_1(tmp_path, n, expected):
    p = create_alphabet_file(tmp_path)

    i = read_n(p, n)
    assert i == iter(i)
    assert len(list(i)) == expected
```

To make sure you keep getting these emails, please add reuven@lerner.co.il to your address book or whitelist us. Want out of the loop? Unsubscribe.

Our postal address: 14 Migdal Oz Street, Apt. #1, Modi'in 71703 Israel
"""
