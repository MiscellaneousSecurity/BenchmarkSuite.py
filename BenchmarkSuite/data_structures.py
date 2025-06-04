import time

def bench_list_append_int(number_of_appends=1_000_000):
    t0 = time.perf_counter()
    lst = []
    for i in range(number_of_appends):
        lst.append(i)
    t1 = time.perf_counter()
    return t1 - t0

def bench_list_comprehension_int(number_of_ints=1_000_000):
    t0 = time.perf_counter()
    lst = [i for i in range(number_of_ints)]
    t1 = time.perf_counter()
    return t1 - t0

def bench_list_append_char(number_of_appends=1_000_000):
    t0 = time.perf_counter()
    lst = []
    for i in range(number_of_appends):
        lst.append(chr(i % 1114111))
    t1 = time.perf_counter()
    return t1 - t0

def bench_list_comprehension_char(number_of_char=1_000_000):
    t0 = time.perf_counter()
    lst = [chr(i % 1114111) for i in range(number_of_char)]
    t1 = time.perf_counter()
    return t1 - t0