import random
from functions import timer
from math import log2


def fast_pow(x, n, mod=None):
    result: int = 1
    m = n
    while n:
        if n % 2:
            result *= m
        m *= m

        n //= 2
        if mod is not None:
            result %= mod
            m %= mod

    if mod is not None:
        result %= mod

    return result


@timer
def farm_check(prime: int) -> bool:
    assert prime > 1
    if prime == 2: return True
    a = random.randint(1, prime - 1)
    steps = 100

    for _ in range(steps):
        if fast_pow(a, prime - 1, prime) != 1:
            return False

    return True


def get_degree(n, p):
    cnt = 0
    while n % p == 0:
        n //= p
        cnt += 1
    return cnt


@timer
def Miller_Rabin_test(prime: int):
    assert prime > 1
    if prime == 2: return True

    k = get_degree(prime - 1, 2)
    v = prime / k
    a = random.randint(1, prime - 1)

    steps = 100

    for _ in range(steps):
        a_pref = fast_pow(a, v, prime)
        for i in range(1, k):
            a

if __name__ == "__main__":
    prime = 545926466721965277795915587252158472989539631833357096907722487284769809236535659520608130930705863868505493239501826016000430201172292906336618761568226983656589345299199572502089691656856047464319903935267805246627790836253855251607174092968344521029424498560725599814602818024570875152179882479421
    assert farm_check(prime)
    print(farm_check.timer)
