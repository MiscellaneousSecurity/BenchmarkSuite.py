import sys, time
from functools import lru_cache
sys.setrecursionlimit(2**31)

def fibonacci_recursion(n:int) -> int:
    assert(isinstance(n, int))
    if n < 2: return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_iteration(n:int) -> int:
    assert(isinstance(n, int))
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@lru_cache(256)
def fibonacci_recursion_cached_256(n:int) -> int:
    assert(isinstance(n, int))
    if n < 2: return n
    return fibonacci_recursion_cached_256(n-1) + fibonacci_recursion_cached_256(n-2)

@lru_cache(16)
def fibonacci_recursion_cached_16(n:int) -> int:
    assert(isinstance(n, int))
    if n < 2: return n