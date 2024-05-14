INF = 2 ** 32


class Table:
    def __init__(self, size: int) -> None:
        n = 1
        while n < size:
            n *= 2

        self.size = n
        self.tree: dict[int: int] = dict()

    def __getitem__(self, idx: int) -> int:
        idx += self.size - 1
        return self._getitem(self.size - 1, 2 * self.size - 1, 0, idx)

    def _getitem(self, l, r, x, idx) -> [int, None]:
        m = (l + r) // 2
        if x not in self.tree:
            return None

        if idx == l:
            return self.tree[x]

        if idx < m:
            return self._getitem(l, m, 2 * x + 1, idx)
        else:
            return self._getitem(m, r, 2 * x + 2, idx)

    def __setitem__(self, idx, x) -> None:
        idx += self.size - 1
        self._setitem(self.size - 1, 2 * self.size - 1, 0, idx, x)

    def _setitem(self, l, r, x, idx, val) -> None:
        m = (l + r) // 2
        if x not in self.tree:
            self.tree[x] = -INF

        if l == idx:
            self.tree[x] = val
        elif idx < m:
            self._setitem(l, m, 2 * x + 1, idx, val)
        else:
            self._setitem(m, r, 2 * x + 2, idx, val)


class HashTable:
    def __init__(self, module=int(1e9)) -> None:
        self.M = module
        if self.M > int(1e6):
            self.table = Table(self.M)
        else:
            self.table = [None] * self.M

    def add(self, x) -> None:
        step = 0
        while True:
            assert step < 1e5

            idx = self._hash(x, step)
            y = self.table.__getitem__(idx)
            if y is None:
                self.table[idx] = x
                return
            elif y == x:
                return

            step += 1

    def find(self, x) -> bool:
        step = 0
        while step < 1e6:
            idx = self._hash(x, step)
            y = self.table.__getitem__(idx)
            if y is None:
                return False
            elif y == x:
                return True
            step += 1

        return False

    def _hash(self, x: int, i: int) -> int:
        a = 13
        b = 17
        c = 5
        d = 1
        return (x * a + b * i + c * (x ^ i) + d) % self.M


if __name__ == "__main__":
    ...
