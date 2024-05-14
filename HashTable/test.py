from hash_table import HashTable
from random import shuffle


def test_hash_table():
    a = HashTable()
    a.add(1)
    a.add(2)
    a.add(3)

    assert a.find(1)
    assert a.find(2)
    assert a.find(3)


def test_small_hash_table():
    def rnd(i: int) -> int:
        return (135419 * i + 84593) % 61884983

    L = int(1e2)

    a = [0] * L

    h = HashTable()

    for i in range(L):
        a[i] = rnd(i)

    for x in a:
        h.add(x)

    for x in a:
        h.add(x)

    for y in map(rnd, range(0, 2 * L)):
        assert (y in a) == h.find(y)


def test_big_hash_table():
    def rnd(i: int) -> int:
        return (135419 * i + 84593) % 61884983

    L = int(1e4)

    a = [0] * L

    h = HashTable()

    for i in range(L):
        a[i] = rnd(i)

    for x in a:
        h.add(x)

    for y in map(rnd, range(0, 2 * L)):
        assert (y in a) == h.find(y)


def test_set():
    def rnd(i: int) -> int:
        return (135419 * i + 84593) % 61884983

    L = int(1e4)

    a = [0] * L

    h = set()

    for i in range(L):
        a[i] = rnd(i)

    for x in a:
        h.add(x)

    for y in map(rnd, range(0, 2 * L)):
        assert (y in a) == (y in h)
