import time


def timer(func):
    def _inner(*args, **kwargs):
        time_start = time.time()
        val = func(*args, **kwargs)
        time_finish = time.time()

        _inner.timer = time_finish - time_start

        return val

    _inner.timer = 0

    return _inner
