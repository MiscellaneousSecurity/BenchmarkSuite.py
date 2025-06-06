import time
from random import randint

def bench_list_append_int(number_of_appends:int=1_000_000) -> float:
    assert(isinstance(number_of_appends, int))
    t0 = time.perf_counter()
    lst = []
    for i in range(number_of_appends):
        lst.append(i)
    t1 = time.perf_counter()
    return t1 - t0

def bench_list_comprehension_int(number_of_ints:int=1_000_000) -> float:
    assert(isinstance(number_of_ints, int))
    t0 = time.perf_counter()
    lst = [i for i in range(number_of_ints)]
    t1 = time.perf_counter()
    return t1 - t0

def bench_list_append_char(number_of_appends:int=1_000_000) -> float:
    assert(isinstance(number_of_appends, int))
    t0 = time.perf_counter()
    lst = []
    for i in range(number_of_appends):
        lst.append(chr(i % 1114111))
    t1 = time.perf_counter()
    return t1 - t0

def bench_list_comprehension_char(number_of_char:int=1_000_000) -> float:
    assert(isinstance(number_of_char, int))
    t0 = time.perf_counter()
    lst = [chr(i % 1114111) for i in range(number_of_char)]
    t1 = time.perf_counter()
    return t1 - t0

def bench_remove_list_duplicates_using_set(size_of_list:int=1_000_000) -> float:
    assert(isinstance(size_of_list, int))
    lst = [randint(0, 6) for _ in range(size_of_list)]
    t0 = time.perf_counter()
    lst = list(set(lst))
    t1 = time.perf_counter()
    return t1 - t0