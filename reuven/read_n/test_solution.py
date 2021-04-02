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


