import time
from typing import Callable


def track_addition_time(x: int, y: int, func: Callable) -> float:
    start = time.time()
    func(x=x, y=y)
    end = time.time()
    return end - start


def mock_slow_addition(x: int, y: int) -> int:
    time.sleep(3)
    return x + y


def mock_fast_addition(x: int, y: int) -> int:
    time.sleep(1)
    return x + y


if __name__ == "__main__":
    x = 2
    y = 5
    slow_addition_time = track_addition_time(x=x, y=y, func=mock_slow_addition)
    fast_addition_time = track_addition_time(x=x, y=y, func=mock_fast_addition)

    print(f"Methode 1: {slow_addition_time}")
    print(f"Methode 2: {fast_addition_time}")
