import sys, time
from functools import lru_cache, cache

sys.setrecursionlimit(2**31)

def fibonacci_recursion(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    if n < 2: return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_iteration(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@lru_cache(256)
def fibonacci_recursion_cached_256(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    if n < 2: return n
    return fibonacci_recursion_cached_256(n-1) + fibonacci_recursion_cached_256(n-2)

@lru_cache(16)
def fibonacci_recursion_cached_16(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    if n < 2: return n
    return fibonacci_recursion_cached_16(n-1) + fibonacci_recursion_cached_16(n-2)

@lru_cache(1024)
def fibonacci_recursion_cached_1024(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    if n < 2: return n
    return fibonacci_recursion_cached_1024(n-1) + fibonacci_recursion_cached_1024(n-2)

@lru_cache(65536)
def fibonacci_recursion_cached_65536(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    if n < 2: return n
    return fibonacci_recursion_cached_65536(n - 1) + fibonacci_recursion_cached_65536(n - 2)

@cache
def fibonacci_recursion_cached_unlimited(n:int) -> int:
    assert(isinstance(n, int) and n>=0)
    if n<2: return n
    return fibonacci_recursion_cached_unlimited(n - 1) + fibonacci_recursion_cached_unlimited(n - 2)

def bench_fibonacci_recursion(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_recursion(n)
    t1 = time.perf_counter()
    return t1 - t0

def bench_fibonacci_iteration(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_iteration(n)
    t1 = time.perf_counter()
    return t1 - t0

def bench_fibonacci_recursion_cached_256(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_recursion_cached_256(n)
    t1 = time.perf_counter()
    return t1 - t0

def bench_fibonacci_recursion_cached_16(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_recursion_cached_16(n)
    t1 = time.perf_counter()
    return t1 - t0

def bench_fibonacci_recursion_cached_1024(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_recursion_cached_1024(n)
    t1 = time.perf_counter()
    return t1 - t0

def bench_fibonacci_recursion_cached_65536(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_recursion_cached_65536(n)
    t1 = time.perf_counter()
    return t1 - t0

def bench_fibonacci_recursion_cached_unlimited(n:int=25) -> float:
    assert(isinstance(n, int) and n>=0)
    t0 = time.perf_counter()
    fibonacci_recursion_cached_unlimited(n)
    t1 = time.perf_counter()
    return t1 - t0
